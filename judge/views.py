from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotFound, HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile

from .models import Submission, Assignment

import subprocess
import os
import json

def evaluate_submission(submitted_file, judge_file):
    result = None
    try:
        result = subprocess.run('python3 {} {}'.format(judge_file, submitted_file), shell=True, timeout=20, check=True, stdout=subprocess.PIPE)
    except Exception as e:
        return 0, str(e)
    result_lines = result.stdout.decode("utf-8").split('\n', 1)
    return int(result_lines[0]), result_lines[1]

@csrf_exempt
@require_http_methods(['POST'])
def upload_file(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    filename, file_extension = os.path.splitext(str(request.FILES['file']))
    name = request.POST.get('name', None)
    
    if file_extension == '.ipynb':
        sources = []
        data = json.load(request.FILES['file'])
        if 'cells' not in data:
            return JsonResponse({ 'score': 0, 'message': 'ipynb is in wrong format' })    
        for cell in data['cells']:
            if cell['cell_type'] == 'code'\
                and len(cell['source']) > 0\
                and cell['source'][0].startswith('# GRADED FUNCTION'):
                sources.extend(cell['source'])
        
        sources_string = '\n'.join(sources)

        submission = Submission.objects.create(uploaded_file=ContentFile(sources_string, name=filename + '.py'), assignment=assignment, name=name)
    else:
        submission = Submission.objects.create(uploaded_file=request.FILES['file'], assignment=assignment, name=name)
    score, message = evaluate_submission(settings.MEDIA_ROOT + submission.uploaded_file.name, settings.MEDIA_ROOT + assignment.judge_file.name)
    submission.score = score
    submission.save()
    return JsonResponse({ 'score': score, 'message': message })

@login_required
def index(request):
    assignments = Assignment.objects.all()
    return render(request, 'index.html', { 'assignments': assignments })
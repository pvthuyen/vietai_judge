from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotFound, HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required

from .models import Submission, Assignment

import subprocess

def evaluate_submission(submitted_file, judge_file):
    result = None
    try:
        result = subprocess.run('python3 {} {}'.format(judge_file, submitted_file), shell=True, timeout=2.5, check=True, stdout=subprocess.PIPE)
    except Exception as e:
        return 0
    result_lines = result.stdout.split('\n', 1)
    return int(result_lines[0]), result_lines[1]

@csrf_exempt
@require_http_methods(['POST'])
def upload_file(request, assignment_id):
    print(request.body)
    assignment = get_object_or_404(Assignment, id=assignment_id)
    submission = Submission.objects.create(uploaded_file=request.FILES['file'], assignment=assignment)
    score, message = evaluate_submission(settings.MEDIA_ROOT + submission.uploaded_file.name, settings.MEDIA_ROOT + assignment.judge_file.name)
    submission.score = score
    submission.save()
    return JsonResponse({ 'score': score, 'message': message })

@login_required
def index(request):
    assignments = Assignment.objects.all()
    return render(request, 'index.html', { 'assignments': assignments })
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotFound, HttpResponse
from django.conf import settings

from .models import Submission

import subprocess

def evaluate_submission(filename):
    result = None
    try:
        result = subprocess.run('python3 {}/test_judge.py {}'.format(settings.BASE_DIR, filename), shell=True, timeout=2.5, check=True, stdout=subprocess.PIPE)
    except Exception as e:
        return JsonResponse({ 'score': 0 })
    return JsonResponse({ 'score': int(result.stdout) })

@csrf_exempt
@require_http_methods(['POST'])
def upload_file(request):
    submission = Submission.objects.create(uploaded_file=request.FILES['file'])
    return evaluate_submission(settings.MEDIA_ROOT + submission.uploaded_file.name)

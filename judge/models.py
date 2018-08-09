from django.db import models
from django.conf import settings

class Assignment(models.Model):
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    judge_file = models.FileField(upload_to='judge/')

class Submission(models.Model):
    # file will be uploaded to MEDIA_ROOT/uploads
    uploaded_file = models.FileField(upload_to='submissions/')
    assignment = models.ForeignKey(Assignment, db_index=True, null=True, related_name='submissions', on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField('score', default=0)
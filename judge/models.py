from django.db import models
from django.conf import settings

class Submission(models.Model):
    # file will be uploaded to MEDIA_ROOT/uploads
    uploaded_file = models.FileField(upload_to='uploads/')
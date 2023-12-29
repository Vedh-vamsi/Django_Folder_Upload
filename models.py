from django.db import models

class Folder(models.Model):
    folder_name = models.CharField(max_length=255)
    uploaded_file = models.FileField(upload_to='uploads/')
  
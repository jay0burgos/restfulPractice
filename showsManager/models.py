from django.db import models

#title network release date

class shows(models.Model):
    title = models.CharField(max_length = 255)
    network = models.CharField(max_length = 255)
    releasedDate = models.DateField()
    discription = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
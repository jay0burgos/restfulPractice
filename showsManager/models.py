from django.db import models

#title network release date
class showValidator(models.Manager):
    def validator(self, post_data):
        errors = {}

        if len(post_data['title']) < 2:
            errors['title'] = "Title needs to be longer"
        if len(post_data['network']) < 2:
            errors['network'] = "Network needs to be longer"
        if len(post_data['discription']) < 10:
            errors['discription'] = "Discription needs to be longer"
        return errors

class shows(models.Model):
    title = models.CharField(max_length = 255)
    network = models.CharField(max_length = 255)
    releasedDate = models.DateField()
    discription = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    #always include this in this verbiage
    objects = showValidator()

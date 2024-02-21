from django.db import models

# Create your models here.
class Profile(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length= 200)
    email = models.CharField(max_length=200)
    summary = models.TextField(max_length = 2000)
    skills = models.CharField(max_length=400)
    education = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    previous_work = models.CharField(max_length=200)



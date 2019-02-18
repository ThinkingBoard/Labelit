from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):

    user = models.ForeignKey(
       User, on_delete=models.CASCADE)

    project_name = models.CharField(max_length=200)

    project_description = models.CharField(max_length=2000)

    pub_date = models.DateTimeField('date published')

    label_type_choices = (('C', 'Classification'), ('R', 'Regression'),)
    label_type = models.CharField(max_length=20, default='', choices=label_type_choices)

    class_labels_values = models.CharField(max_length=2000)

    def __str__(self):
        return self.project_name
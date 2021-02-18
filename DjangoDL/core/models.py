from django.db import models
from .validators import json_validator
# Create your models here.


class DeepLearningModel(models.Model):

    model = models.FileField(upload_to="models")
    transformations = models.JSONField(default = dict, validators=[json_validator])

class Inference(models.Model):

    model = models.ForeignKey('DeepLearningModel', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images")

class Result(models.Model):

    res = models.CharField(max_length=256)
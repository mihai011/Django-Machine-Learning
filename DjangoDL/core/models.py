from django.db import models

# Create your models here.


class DeepLearningModel(models.Model):

    model = models.FileField(upload_to="models")
    transformations = models.JSONField(default = dict)

class Inference(models.Model):

    model = models.ForeignKey('DeepLearningModel', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images")
from django.db import models

# Create your models here.


class DeepLearningModel(models.Model):

    model = models.FileField()
    transformations = models.JSONField(default = dict)

class Inference(models.Model):

    model = models.ForeignKey('DeepLearningModel', on_delete=models.CASCADE)
    image = models.ImageField()




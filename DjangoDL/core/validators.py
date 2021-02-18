import json
import torchvision.transforms as transforms

from django.core.exceptions import ValidationError

def json_validator(value):

    t = [str(t) for t in transforms.__dict__]
    wrong_transforms = []

    for k,v in value.items():

        if k not in t:
            wrong_transforms.append(k)


    if len(wrong_transforms) == 0:
        return True

    raise ValidationError(
        ('Invalid tranformations:'+str(wrong_transforms)))
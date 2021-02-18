import string


from celery import shared_task

from .models import Inference
from .models import Result

@shared_task
def make_inference(inference_id):

    inf = Inference.objects.get(id = inference_id)

    res = Result(res="test")

    res.save()

    return True

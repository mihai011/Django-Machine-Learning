import string
import os
from celery import shared_task

from .models import Inference
from .models import Result



import io
import torch 
import torchvision.transforms as transforms
from PIL import Image

def transform_image(image_bytes, tt):
    my_transforms = tt
    # my_transforms = transforms.Compose([transforms.Resize(255),
    #                                     transforms.CenterCrop(224),
    #                                     transforms.ToTensor(),
    #                                     transforms.Normalize(
    #                                         [0.485, 0.456, 0.406],
    #                                         [0.229, 0.224, 0.225])])
    image = Image.open(io.BytesIO(image_bytes))
    return my_transforms(image).unsqueeze(0)

def load_checkpoint(filepath):
    checkpoint = torch.load(filepath)
    model = checkpoint['model']
    model.load_state_dict(checkpoint['state_dict'])
    for parameter in model.parameters():
        parameter.requires_grad = False

    model.eval()
    return model


def get_prediction(image,model):
    outputs = model.forward(image)
    _, y_hat = outputs.max(1)
    return y_hat

@shared_task
def make_inference(inference_id):

    inf = Inference.objects.get(id = inference_id)

    transformations = inf.model.transformations

    tt = []

    for t in transformations.keys():
        
        found = None
        for pos in transforms.__dict__:
            if t == str(pos):
                found = getattr(transforms, t)
                break
        if found:
            print(t)
            if t == "ToTensor":
                tt.append(found())
                continue
            if t == "Normalize":
                tt.append(found(*transformations[t]))
                continue
            tt.append(found(transformations[t]))
    
    print(tt)

    tt = transforms.Compose(tt)

    with open(str(inf.image.file), "rb") as f:
        image_bytes = f.read()
    
    image = transform_image(image_bytes, tt)


    model = load_checkpoint(str(inf.model.model.file))

    res = get_prediction(image, model)
    res = Result(res=str(res))

    res.save()

    return os.getcwd()

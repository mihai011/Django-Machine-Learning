from django.shortcuts import render
from .forms import InferenceForm, ModelForm
from .models import Inference, DeepLearningModel

from .models import Result
from .tasks import make_inference
# Create your views here.


def main(request):

    context = {}
    context['form'] = InferenceForm()

    if request.method == 'POST':
        form = InferenceForm(request.POST)
        if form.is_valid():
            inf = Inference(form)
            inf.save()
            return render(request, template_name='main.html', context=context)

    return render(request, template_name='main.html', context=context)

def model(request):

    context = {}
    context['form'] = ModelForm()

    if request.method == 'POST':
        form = ModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return render(request, template_name='form.html', context=context)
        else:
            errors = form.errors["transformations"]
            context["message"]  = errors

    return render(request, template_name='form.html', context=context)



def inference(request):
    context = {}
    context['form'] = InferenceForm()

    if request.method == 'POST':
        form = InferenceForm(request.POST, request.FILES)
        if form.is_valid():
            inf = form.save(commit=True)
            make_inference.delay(inf.id)
            return render(request, template_name='form.html', context=context)
    
    results = Result.objects.all()
    context["objects"] = [r.res for r in results]

    return render(request, template_name='form.html', context=context)

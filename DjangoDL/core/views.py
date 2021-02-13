from django.shortcuts import render
from .forms import InferenceForm, ModelForm
from .models import Inference, DeepLearningModel
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

    return render(request, template_name='form.html', context=context)



def inference(request):
    context = {}
    context['form'] = InferenceForm()

    if request.method == 'POST':
        form = InferenceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return render(request, template_name='form.html', context=context)

    return render(request, template_name='form.html', context=context)

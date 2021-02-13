from django.forms import ModelForm
from .models import Inference, DeepLearningModel

class InferenceForm(ModelForm):

    class Meta:

        model = Inference   
        fields = ("__all__")

class ModelForm(ModelForm):

    class Meta:

        model = DeepLearningModel
        fields = ("__all__")
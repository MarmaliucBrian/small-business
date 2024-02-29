from django.forms import ModelForm

from servicii.models import ServiciiModels


class ServiciiForm(ModelForm):

    class Meta:
        model = ServiciiModels
        fields = '__all__'
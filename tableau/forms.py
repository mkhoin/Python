from django.utils.translation import ugettext_lazy as _
from .models import *
from django import forms


class imageForm(forms.ModelForm):
    class Meta:
        model = image
        fields = ('image1','image2','image3',)

    def save(self, commit=True):
        imagedata = super(imageForm, self).save(commit=False)
        if commit:
            imagedata.save()
        return imagedata

from django.utils.translation import ugettext_lazy as _
from .models import *
from django import forms


class email_infoForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=70)), label=_("이메일")) #이메일입력

    class Meta:
        model = email_info
        fields = ('email',)

    def save(self, commit=True): #저장
        Email = super(email_infoForm, self).save(commit=False)
        if commit:
            Email.save()
        return Email

class imageForm(forms.ModelForm):

    class Meta:
        model = image
        fields = ('image1','image2','image3',)

    def save(self, commit=True):
        Imageform = super(imageForm, self).save(commit=False)

        if commit:
            Imageform.save()
        return Imageform

from django.shortcuts import render
from .forms import *
from django.http import HttpResponseRedirect

def index(request):
    if request.method == "POST":
        emailform = email_infoForm(request.POST)
        if emailform.is_valid():
            email = emailform.save(commit=False)
            email.save()
            return HttpResponseRedirect('/upload/')
    else:
        emailform = email_infoForm()
    return render(request, 'index.html', {'emailform': emailform})

def upload(request):
    if request.method == "POST":
        upimage=imageForm(request.POST)
        emailform = email_infoForm()
        if upimage.is_valid():
            uploadimage = upimage.save(commit=False)
            uploadimage.save()
            return HttpResponseRedirect('/result/')
    else:
        upimage = imageForm()
    return render(request, 'upload.html', {'upimage': upimage})

def result(request):
    return render(request, 'result.html')
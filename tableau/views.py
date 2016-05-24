from django.shortcuts import render
from .forms import *
from django.http import HttpResponseRedirect

def index(request):
    if request.method == "POST":
        upimage=imageForm(request.POST)
        if upimage.is_valid():
            uploadimage = upimage.save(commit=False)
            uploadimage.save()
            return HttpResponseRedirect('/result/')
    else:
        upimage = imageForm()
    return render(request, 'upload.html', {'upimage': upimage})

def result(request):
    return render(request, 'result.html')
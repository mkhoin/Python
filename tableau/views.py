from django.shortcuts import render

from django.http import *
import random
import string
from .analyze import *

from .forms import *
from django.http import *
import random
import string


def mk_random_str(length=10):
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))


def index(request):
    files = []
    result = []
    if request.method == "POST":
        for file in request.FILES.keys():
            fname = mk_random_str(length=30)
            files.append(fname)
            with open('./upload/%s' % fname, 'wb') as destination:
                for chunk in request.FILES[file].chunks():
                    destination.write(chunk)
                    result.append(list(colorz('./upload/%s' % fname)))
        return HttpResponse('%s uploaded!' %result)
    return render(request, 'upload.html')

def result(request):
    return render(request, 'result.html')
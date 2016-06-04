from django.shortcuts import render
<<<<<<< HEAD
from django.http import *
import random
import string
from .analyze import *
=======
from .forms import *
from django.http import *
import random
import string

>>>>>>> bf4897fb65dbcdfd0ac550caf6e249e4d8257e45
def mk_random_str(length=10):
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))


def index(request):
    files = []
    if request.method == "POST":
        for file in request.FILES.keys():
            fname = mk_random_str(length=30)
            files.append(fname)
            with open('./upload/%s' % fname, 'wb') as destination:
                for chunk in request.FILES[file].chunks():
                    destination.write(chunk)
<<<<<<< HEAD
                    result=list(colorz('./upload/%s' % fname))
        return HttpResponse('%s uploaded!' %result)
=======
        return HttpResponse('./upload/%s uploaded!' % files)
>>>>>>> bf4897fb65dbcdfd0ac550caf6e249e4d8257e45
    return render(request, 'upload.html')

def result(request):
    return render(request, 'result.html')
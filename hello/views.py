from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

import requests
import os

# Create your views here.
def index(request):
    r = requests.get('http://httpbin.org/status/418')
    N = os.getenv('TIMES', 5)
    rsp = '<pre>' + r.text + '</pre>'

    return HttpResponse(rsp * int(N))


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

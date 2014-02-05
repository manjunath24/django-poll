from django.shortcuts import render
from pollapp.models import Poll, Choice
import socket
# Create your views here.


def index(request):
    data = Poll.objects.all().order_by('-pub_date')
    return render(request, 'index.html', {'data': data, 'home': True})


def about(request):
    return render(request, 'about.html', {'about': True})

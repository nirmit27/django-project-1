# Create your views here.
from django.shortcuts import render


def pnav_view(request):
    params = {
        'name': 'Nirmit Mishra',
        'date': 'April 6th, 2023'
    }
    return render(request, 'pnav.html', params)


def text_view(request):
    return render(request, 'text.html')

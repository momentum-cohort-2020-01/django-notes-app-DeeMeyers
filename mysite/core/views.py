from django.shortcuts import render
from django.http import HttpResponse

import data

# Create your views here.
def index(request):
    context = data.NOTES
    return render(request, 'base.html', context)
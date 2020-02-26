from django.shortcuts import render
from django.http import HttpResponse

from .models import Notes

# Create your views here.


def notes_list(request):
    notes = Notes.objects.all()
    return render(request, 'core/notes_list.html', {"notes": notes})


def notes_detail(request, pk):
    note = Notes.objects.get(pk=pk)
    return render(request, 'core/notes_detail.html', {"note": note, "pk": pk})

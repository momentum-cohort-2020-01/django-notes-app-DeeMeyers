from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Notes
from .forms import NotesForm

# Create your views here.


def notes_list(request):
    notes = Notes.objects.all()
    return render(request, 'core/notes_list.html', {"notes": notes})


def notes_details(request, pk):
    note = Notes.objects.get(pk=pk)
    return render(request, 'core/notes_details.html', {"note": note, "pk": pk})

def notes_form(request):
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            note = form.save()
            return redirect('notes_details', pk=note.pk)
    else:
        form = NotesForm()
    
    return render(request, 'core/notes_form.html', {"form": form})

def notes_edit(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    if request.method == 'POST':
        form = NotesForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes_details', pk=note.pk)
    else:
        form = NotesForm(instance=note)
    
    return render(request, 'core/notes_edit.html', {"form": form})


def notes_delete(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    note.delete()
    return redirect('notes_list')
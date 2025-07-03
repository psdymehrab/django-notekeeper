from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from notes.forms import NoteForm
from notes.models import Note


# Create your views here.
@login_required
def note_view(request):
    notes = Note.objects.filter(user=request.user)
    return render(request,'notes/notes_list.html',{'notes':notes})

@login_required
def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('notes:note_list')
        else:
            return render(request, 'notes/note_form.html', {'form': form})
    else:
        form = NoteForm()
        return render(request, 'notes/note_form.html', {'form': form})

@login_required
def delete_note(request, note_id):
    if request.method == 'GET':
        note = get_object_or_404(Note, id=note_id)
        if note.user == request.user:
            note.delete()
            return redirect('notes:note_list')
        else:
            return redirect('notes:note_list')
    else:
        return redirect('notes:note_list')

@login_required
def update_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)

    if note.user != request.user:
        return redirect('notes:note_list')

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('notes:note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form': form})
from django import forms

from notes.models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
            'title',
            'content',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'عنوان یادداشت:',
            'content': 'متن یادداشت:',
        }
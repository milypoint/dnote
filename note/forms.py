from django import forms


class NoteForm(forms.Form):
	post = forms.CharField(label='', widget=forms.TextInput)
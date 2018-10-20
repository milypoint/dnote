from django.shortcuts import render
from django.views.generic import View
from note.models import Note
from note.forms import NoteForm


class Index(View):
	tamplate_name = 'mainpage.html'

	def get(self, request, *args, **kwards):
		form = NoteForm()

		return render(request, self.tamplate_name, {
			'notes' : Note.objects.all().order_by("-unique_word_count"),
			'form' : form
			})

	def post(self, request):
		form = NoteForm(request.POST)

		if form.is_valid():
			text = form.cleaned_data['post']
			print("Add new note:", text)
			note = Note()
			note.text_message = text
			note.save()
			form = NoteForm() # Clear input field 

		return render(request, self.tamplate_name, {
			'notes' : Note.objects.all().order_by("-unique_word_count"),
			'form' : form
			})

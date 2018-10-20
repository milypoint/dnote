from django.db import models


class Note(models.Model):

	@property
	def text_message(self):
		return self.text

	@text_message.setter
	def text_message(self, value):
		'''
		This "property setter" using for automatically calculate and save unique word count in text of note whenever note itself has been added.
		'''

		# Set text value
		self.text = value

		# ...and calculate unique word count
		unique_words = set()
		for word in self.text.split():
			unique_words.add(word)
		unique_word_count = len(unique_words)
		self.unique_word_count = unique_word_count

	# Django model fields:
	text = models.TextField()
	unique_word_count = models.IntegerField()

	def __str__(self): 
		return self.text


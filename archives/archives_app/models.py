from django.db import models

# Create your models here.

class Category(models.Model):
	"""
	Model representing the category to which books and other sub-categories belong. (eg: AI, Algorithms etc.)
	"""

	name = models.CharField(max_length=200, help_text="Enter a category name")
	subdirs = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)

	class Meta:
		verbose_name_plural = "categories"

	def __str__(self):
		"""
		String for representing the model object(in Admin site etc.)
		"""
		return self.name

class Book(models.Model):
	"""
	Model representing a book (but not a specific copy of a book).
	"""
	title = models.CharField(max_length=200)
	path = models.CharField(max_length=256)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
	last_viewed = models.DateTimeField(null=True, blank=True)
	STATUS = (
		('n', 'Not Started'),
		('o', 'Ongoing'),
		('p', 'Paused'),
		('c', 'Complete'),
	)
	status = models.CharField(max_length=1, choices=STATUS, blank=True, default='n', help_text='Reading status')

	class Meta:
		ordering = ["last_viewed"]


	def __str__(self):
		"""
		String for representing the Model object.
		"""
		return self.title

	def get_absolute_url(self):
		"""
		Returns the url to access a detail record for this book.
		"""
		return reverse('book-detail', args=[str(self.id)])
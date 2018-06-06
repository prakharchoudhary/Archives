"""
Script to populate database with all the books and categories(directories)

#TODO:
1. Simply create entries for all books and categories in the database using os.walk().
2. Keep track of all the dirs and books by saving path names of already present ones,
such that only the new ones are appended in the database.
3. Once again use os.walk(), to update the relationship.
"""

import os
from .models import Category, Book
from pprint import pprint
from django.db.utils import IntegrityError

class DBwriter:

	roots = []
	directories = []
	books = []

	def __init__(self, cursor, dir_path):
		self.cur = cursor
		self.path = dir_path

	def get_all_items(self):
		'''
		prepare data structures to store all the dirs and books
		with parent alongside.
		'''
		for root, dirs, files in os.walk(self.path):
			rootname = root.split('/')[-1]
			self.roots.append((root, rootname))
			for d in dirs:
				self.directories.append((rootname, d))
			for file in files:
				self.books.append((rootname, file))

	def gen_categories(self):
		'''
		Use the roots list to make the entries for all categories
		'''
		for root in self.roots:
			cat = Category(name=root[1], path=root[0])
			cat.save()
		self._update_relations()	# this call updates the parent child 
									# relation among dirs.

	def _update_relations(self):
		'''
		Use the directories list to update the parent-child relations between
		categories
		'''
		for dirr in self.directories:
			parent = Category.objects.get(name=dirr[0])
			child = Category.objects.get(name=dirr[1])
			parent.category_set.add(child)

	def gen_books(self):
		'''
		Use the books list to make entries and assign parent directories.
		'''
		books = Book.objects.all()
		allBooks = [b.title for b in books]
		for bookIn in self.books:
			try:
				cat = Category.objects.get(name=bookIn[0])
			except Exception as e:
				print(e)
			bpath = os.path.join(cat.path, bookIn[1])
			try:
				if bookIn[1] not in allBooks:
					cat.book_set.create(title=bookIn[1],path=bpath)
			except IntegrityError:	# incase another book with same name exists
				continue

	def populate_db(self):
		'''
		Main function that populates the database.
		'''
		self.get_all_items()
		self.gen_categories()
		self.gen_books()


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

class Traverse:

	roots = []
	directories = []
	books = []

	def __init__(self, cursor, dir_path, category_table, books_table):
		self.cur = cursor
		self.path = dir_path
		self.category_table = category_table
		self.books_table = books_table

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

	def _update_relations(self):
		'''
		Use the directories list to update the parent-child relations between
		categories
		'''
		pass 
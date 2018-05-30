import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
	"""
	Returns the user object for given user_id.
	"""
	return User.query.get(int(user_id))

class Category(db.Model):
	"""
	id: The primary Key
	name: Name of the category
	subdirs: One-to-many relationship with other categories that fall 
			under it as subdirs
	books: One-to-many relationship with books that are stored directly in them.
	"""
	__tablename__ = 'category'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)
	subdirs = db.relationship("Category", back_populates='category')
	books = db.relationship("Book", back_populates='category')

	def __repr__(self):
		"""
		Print the category name with count of subdirs and books in it.
		"""
		pass

class Book(db.Model):
	__tablename__ = 'books'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(128), unique=True)
	status = db.Column(db.String(16), nullable=False)
	category_id = db.Column(db.Integer, db.ForeignKey('category.id'),
		nullable=False)
	last_viewed = db.Column(db.Datetime, nullable=True)

	def update_status(self, status):
		self.status = status

	def update_last_viewed():
		self.last_viewed = datetime.datatime.utcnow()

	def __repr__(self):
		"""
		Print:
		- Book name
		- Parent directory
		- Status
		- Last Viewed
		"""
		pass

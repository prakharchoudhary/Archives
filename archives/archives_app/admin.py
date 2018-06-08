from django.contrib import admin
from .models import Category, Book
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'path', 'parent')
	list_filter = ('parent',)
	search_fields = ('name', 'parent')

class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'status')
	list_filter = ('category', 'status')
	list_editable = ('status',)
	search_fields = ('title', 'category__name', 'status')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
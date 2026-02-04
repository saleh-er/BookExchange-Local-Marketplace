from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'condition', 'seller')
    search_fields = ('title', 'author')
    list_filter = ('condition',)

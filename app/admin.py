from django.contrib import admin
from .models import Author, Category, Post

# регистрация базы данных
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)

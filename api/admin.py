from django.contrib import admin
from api.models import(Post, Comment, Category, Contact)

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Contact)
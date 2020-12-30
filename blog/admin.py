from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
 	list_display = ('title', 'author', 'created_date')
 	fields = (('title', 'author'), 'text', 'created_date', 'published_date')
 	list_filter = ('title', 'author')

admin.site.register(Post, PostAdmin)



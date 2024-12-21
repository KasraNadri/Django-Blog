from django.contrib import admin
from .models import Post, Author, Tag

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ('author', 'tags', 'created_date')
    list_display = ('title', 'created_date', 'author')
    prepopulated_fields = {"slug": ("title",)}
    
admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
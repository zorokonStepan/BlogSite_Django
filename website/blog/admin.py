from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'date_posted')
    list_filter = ('category', 'author', 'date_posted')


admin.site.register(Post, PostAdmin)

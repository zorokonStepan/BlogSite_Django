from django.contrib import admin

from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'image')
    list_filter = ('user', 'image')


admin.site.register(Profile, ProfileAdmin)

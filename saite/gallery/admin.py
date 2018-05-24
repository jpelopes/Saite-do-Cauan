from django import forms
from django.contrib import admin

from .models import Album, Photo, Contact, Settings, Page, BackgroundImage, Bio

admin.site.register(Album)
admin.site.register(Photo)
admin.site.register(Contact)
admin.site.register(Settings)
admin.site.register(Page)
admin.site.register(BackgroundImage)
admin.site.register(Bio)
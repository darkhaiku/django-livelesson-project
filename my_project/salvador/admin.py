from django.contrib import admin

# Register your models here.

from .models import Album, Track

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('album_name', 'artist')

@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('album', 'order', 'title', 'duration')
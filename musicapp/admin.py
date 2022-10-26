from django.contrib import admin
from .models import Song, Lyric, Artiste
# Register your models here.
admin.site.register(Song)
admin.site.register(Lyric)
admin.site.register(Artiste)
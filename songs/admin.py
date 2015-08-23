from django.contrib import admin

from .models import Song, Performer

class SongInline(admin.StackedInline):
    model = Song

class PerformerAdmin(admin.ModelAdmin):
    inlines = [SongInline,]

admin.site.register(Performer, PerformerAdmin)
admin.site.register(Song)

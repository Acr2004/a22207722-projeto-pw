from django.contrib import admin
from django.utils.html import format_html
from .models import Banda, Album, Musica

class BandaAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_photo', 'foundation')
    search_fields = ('name', 'foundation')
    ordering = ('name',)

    def show_photo(self, obj):
        return format_html('<img src="{}" style="width: 50px; height: 50px">', obj.image.url)
    show_photo.short_description = "Foto da Banda"

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_photo', 'dataDeCriacao', 'banda')
    search_fields = ('name', 'dataDeCriacao', 'banda')
    ordering = ('name', 'banda')

    def show_photo(self, obj):
        return format_html('<img src="{}" style="width: 50px; height: 50px">', obj.image.url)
    show_photo.short_description = "Foto do Album"

class MusicaAdmin(admin.ModelAdmin):
    list_display = ('name', 'spotify_link', 'album')
    search_fields = ('name', 'album')
    ordering = ('name', 'album')

admin.site.register(Banda, BandaAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Musica, MusicaAdmin)
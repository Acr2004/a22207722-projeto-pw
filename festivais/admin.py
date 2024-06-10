from django.contrib import admin
from django.utils.html import format_html
from .models import Localizacao, Banda, Festival

class LocalizacaoAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

class BandaAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

class FestivalAdmin(admin.ModelAdmin):
    list_display = ('name', 'localizacao')
    search_fields = ('name', 'localizacao')
    ordering = ('localizacao', 'name')

    def show_photo(self, obj):
        return format_html('<img src="{}" style="width: 50px; height: 50px">', obj.image.url)
    show_photo.short_description = "Foto do Festival"

admin.site.register(Localizacao, LocalizacaoAdmin)
admin.site.register(Banda, BandaAdmin)
admin.site.register(Festival, FestivalAdmin)
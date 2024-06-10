from django.contrib import admin
from django.utils.html import format_html
from .models import Autor, Artigo, Comentario

class AutorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')
    search_fields = ('name',)
    ordering = ('name',)

class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('title', 'autor', 'data')
    search_fields = ('title', 'autor')
    ordering = ('title', 'autor')

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('autor', 'artigo', 'classf', 'data')
    search_fields = ('autor', 'artigo', 'classf')
    ordering = ('artigo', 'autor', 'classf')

admin.site.register(Autor, AutorAdmin)
admin.site.register(Artigo, ArtigoAdmin)
admin.site.register(Comentario, ComentarioAdmin)
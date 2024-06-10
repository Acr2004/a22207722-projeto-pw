from django.contrib import admin
from django.utils.html import format_html
from .models import Pessoa

admin.site.register(Pessoa)
from django import forms
from .models import Autor, Artigo, Comentario

class AutorForm(forms.ModelForm):
  class Meta:
    model = Autor
    fields = '__all__'

class ArtigoForm(forms.ModelForm):
  class Meta:
    model = Artigo
    fields = '__all__'

class ComentarioForm(forms.ModelForm):
  class Meta:
    model = Comentario
    fields = '__all__'
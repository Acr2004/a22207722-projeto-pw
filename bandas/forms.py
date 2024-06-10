from django import forms
from .models import Banda, Album, Musica

class BandaForm(forms.ModelForm):
  class Meta:
    model = Banda
    fields = '__all__'
    
class AlbumForm(forms.ModelForm):
  class Meta:
    model = Album
    fields = '__all__'
    
class MusicaForm(forms.ModelForm):
  class Meta:
    model = Musica
    fields = '__all__'
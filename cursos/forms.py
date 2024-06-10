from django import forms
from .models import Curso, Disciplina, Projeto, Linguagem, Docente

class CursoForm(forms.ModelForm):
  class Meta:
    model = Curso
    fields = '__all__'

class DisciplinaForm(forms.ModelForm):
  class Meta:
    model = Disciplina
    fields = '__all__'

class ProjetoForm(forms.ModelForm):
  class Meta:
    model = Projeto
    fields = '__all__'

class LinguagemForm(forms.ModelForm):
  class Meta:
    model = Linguagem
    fields = '__all__'

class DocenteForm(forms.ModelForm):
  class Meta:
    model = Docente
    fields = '__all__'
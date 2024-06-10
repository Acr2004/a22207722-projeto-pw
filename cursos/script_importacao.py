import os
import json

from django.db import transaction
from cursos.models import Curso, Disciplina

def importar_curso(archive_name):
    try:
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(diretorio_atual, archive_name)

        with open(path, 'r') as f:
            data = json.load(f)

            with transaction.atomic():
                detalhes_curso = data['courseDetail']
                curso, created = Curso.objects.get_or_create(
                    name = detalhes_curso['courseName'],
                    ap = detalhes_curso['presentation'],
                    objectives = detalhes_curso['objectives'],
                    comp = detalhes_curso['competences']
                )

                for disciplina_data in data['courseFlatPlan']:
                    disciplina, created = Disciplina.objects.get_or_create(
                        name = disciplina_data['curricularUnitName'],
                        year = disciplina_data['curricularYear'],
                        semestre = disciplina_data['semester'],
                        ects = disciplina_data['ects'],
                        curso = curso
                    )

        print("Importação compleata")
    except Exception as e:
        print(f"Error: {e}")
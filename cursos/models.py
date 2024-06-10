from django.db import models

class Curso(models.Model):
    name = models.CharField(max_length=255)
    ap = models.TextField()
    objectives = models.TextField()
    comp = models.TextField()

    def __str__(self):
        return self.name

class Disciplina(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    semestre = models.CharField(max_length=20)
    ects = models.IntegerField()

    def __str__(self):
        return self.name

class Projeto(models.Model):
    name = models.CharField(max_length=255)
    disciplina = models.OneToOneField(Disciplina, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='imagens/', null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

class Linguagem(models.Model):
    name = models.CharField(max_length=50)
    projects = models.ManyToManyField(Projeto)

    def __str__(self):
        return self.name

class Docente(models.Model):
    name = models.CharField(max_length=255)
    disciplinas = models.ManyToManyField(Disciplina)

    def __str__(self):
        return self.name
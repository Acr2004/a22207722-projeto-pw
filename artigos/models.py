from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

class Autor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return f'{self.name} - {self.age} anos'

class Artigo(models.Model):
    title = models.CharField(max_length=100)
    post = models.TextField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, null=True)
    data = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f'{self.title} - {self.autor.name}'

class Comentario(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, null=True)
    comment = models.TextField()
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, null=True)
    classf = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)
    data = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f'{self.autor.name} - {self.artigo.title}'
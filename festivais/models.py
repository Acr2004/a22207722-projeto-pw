from django.db import models

class Localizacao(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Banda(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Festival(models.Model):
    name = models.CharField(max_length=255)
    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE)
    bandas =  models.ManyToManyField(Banda)
    img = models.ImageField(upload_to='imagens/', null=True, blank=True)

    def __str__(self):
        return self.name
from django.db import models
import datetime

class Banda(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='bandas/images/')
    foundation = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f'{self.name} - Fundada em {self.foundation}'

    def get_img(self):
        return self.image.url

class Album(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='bandas/images/')
    dataDeCriacao = models.DateField(default=datetime.date.today)
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.banda.name} - {self.name}'

class Musica(models.Model):
    name = models.CharField(max_length=100)
    spotify_link = models.URLField(null=True, blank=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.name} - {self.album.banda.name} | {self.album.name}'
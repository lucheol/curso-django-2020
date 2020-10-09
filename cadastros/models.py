from django.db import models

# Create your models here.


class Cidade(models.Model):

    nome = models.CharField(max_length=100, unique=True)
    capital = models.BooleanField(default=False, help_text='Marcar se a cidade for capital')

    def __str__(self):

        return self.nome



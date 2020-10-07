from django.db import models

# Create your models here.


class Cidade(models.Model):

    nome = models.CharField(max_length=100)
    capital = models.BooleanField(default=False)

    def __str__(self):

        return self.nome



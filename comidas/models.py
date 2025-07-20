from django.db import models

# Create your models here.
class Comida(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    foto_url = models.URLField(max_length=300, blank = True, null = True)
    data_criacao = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nome
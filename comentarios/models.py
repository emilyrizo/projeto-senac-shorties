from django.db import models

# Create your models here.

class Pessoa(models.Model):
    id_pessoa = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    comentario = models.EmailField(max_length=500)

    def __str__(self):
        return self.nome
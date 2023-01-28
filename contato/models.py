from django.db import models

from usuario.models import Usuario


# Create your models here.
class Contato(models.Model):
    Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    telefone = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.nome}"

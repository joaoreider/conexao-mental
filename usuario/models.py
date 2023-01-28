from django.db import models


# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return f"{self.nome}"

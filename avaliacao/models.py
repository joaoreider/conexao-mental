from django.db import models
from datetime import datetime


class Avaliacao(models.Model):

    choices = (
        ('p', 'Péssimo'),
        ('r', 'Ruim'),
        ('b', 'Bom'),
        ('o', 'Ótimo')
    )

    data = models.DateTimeField(default = datetime.now)

    nome = models.CharField(max_length = 100, blank= True, null=True)

    avaliacao_dia = models.CharField(max_length=10, choices=choices, blank= True, null=True)


    def __str__(self) -> str:
        return f"{self.nome} | {self.avaliacao_dia}"


class Acontecimentos(models.Model):

    usuario = models.ForeignKey(Avaliacao, on_delete = models.DO_NOTHING)

    choices = (
        ('p', 'Positivo'),
        ('n', 'Negativo'),
    )
    tipo_acontecimento = models.CharField(max_length=10, choices=choices, blank= True, null=True)

    descricao_acontecimento = models.TextField(blank= True, null=True)


    def __str__(self) -> str:
        return self.tipo_acontecimento
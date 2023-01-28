from django.db import models

from usuario.models import Usuario


# Create your models here.
class Alerta(models.Model):
    choice_alrerta = (('p', 'Pânico'), ('a', 'Ansiedade'), ('d', 'Depressão'))
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    tipo_alerta = models.Choices(choice_alrerta)
    horario_inicio_alerta = models.DateTimeField(auto_now=True)
    horario_fim_alerta = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return self.choice_alrerta

from django.db import models


# Create your models here.
class Clients(models.Model):
    name = models.CharField("Nombre", max_length=128)
    web = models.CharField("Direccion Web", max_length=128)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return f"{self.name}"

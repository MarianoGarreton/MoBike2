
from django.db import models

# Create your models here.

class Usuario(models.Model):
    RutUsuario = models.CharField(max_length=8)
    DvUsuario = models.CharField(max_length=1)
    Nombre = models.CharField(max_length=100)
    ApellidoPaterno = models.CharField(max_length=50)
    ApellidoMaterno = models.CharField(max_length=50)
    Direccion = models.CharField(max_length=250)
    Email = models.CharField(max_length=250)
    telefono = models.CharField(max_length=12)
    CodComuna = models.IntegerField(4)
    Password = models.CharField(max_length=50)

    def NombreCompleto(self):
        cadena="(3) (4), (5)"
        return cadena.format(self.Nombre,self.ApellidoPaterno,self.ApellidoMaterno)

    def __str__(self):
        return self.NombreCompleto()

class TipoUsuario(models.Model):
    CodUsuario = models.IntegerField(max_length=5)
    Descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.Descripcion

class UsuarioTipo(models.Model):
    Usuario=models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    TipoUsuario = models.ForeignKey(TipoUsuario, null=False, blank=False,
                                    on_delete=models.CASCADE)


class Comuna(models.Model):
    CodComuna = models.IntegerField(max_length=3)
    Descripcion = models.CharField(max_length=150)

    def __str__(self):
        return self.Descripcion

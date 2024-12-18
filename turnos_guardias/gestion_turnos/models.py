from django.db import models
from django.contrib.auth.models import User



class Guardia(models.Model):
    PREFERENCIAS_TURNOS = [
    (1, "Mañana"),
    (2, "Tarde"),
    (3, "Noche"),
]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=255)
    latitud = models.FloatField(null=True, blank=True)
    longitud = models.FloatField(null=True, blank=True)
    disponibilidad_horas = models.IntegerField()
    activo = models.BooleanField(default=True)
    preferencia_turno = models.IntegerField(choices=PREFERENCIAS_TURNOS, default=1)

    def __str__(self):
        return self.user.username

class AsignacionNotificacion(models.Model):
    guardia = models.ForeignKey(User, on_delete=models.CASCADE)
    sucursal = models.ForeignKey('Sucursal', on_delete=models.CASCADE)
    turno = models.IntegerField()  # 1 = Mañana, 2 = Tarde, 3 = Noche
    estado = models.CharField(
        max_length=10,
        choices=[('pendiente', 'Pendiente'), ('aceptada', 'Aceptada'), ('rechazada', 'Rechazada')],
        default='pendiente'
    )
    fecha_envio = models.DateTimeField(auto_now_add=True)
    
class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    latitud = models.FloatField(null=True, blank=True)
    longitud = models.FloatField(null=True, blank=True)
    requerimiento_turnos = models.IntegerField()

    def __str__(self):
        return self.nombre

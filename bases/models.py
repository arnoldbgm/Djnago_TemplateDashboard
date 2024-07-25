from django.db import models
from django.contrib.auth.models import User


# A continuacion crearemos un modelo que va a ser heredado por todos los modelos del proyecto
class ClaseModelo(models.Model):
   estado = models.BooleanField(default=True)
   fecha_creacion = models.DateTimeField(auto_now_add=True)
   fecha_modificacion = models.DateTimeField(auto_now=True)
   user_creacion = models.ForeignKey(User,on_delete=models.CASCADE)
   user_modificacion = models.IntegerField(blank=True, null=True)

   class Meta:
      abstract = True # Con esto Django ya no va a tomar en cuenta a la hora de crear una migracion
      
from django.db import models

from bases.models import ClaseModelo

class CatgoriaModel(ClaseModelo):
   descripcion = models.CharField(max_length=100, help_text='Descripcion', unique=True)

   def __str__(self) -> str:
      return f"{self.descripcion}"
   
   # Ahora si queremos que se guarde en mayuscula debemos hacerlo desde el modelo
   def save(self):
      self.descripcion = self.descripcion.upper()
      # Otra opcion con una sintaxis mas clara es usar
      # super().save()
      super(CatgoriaModel, self).save()

   class Meta:
      verbose_name_plural = "Categorias"
      db_table = "categorias"
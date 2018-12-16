# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Creamos nuestros modelos aquí.
# Articulo, contiene información de los artículos que vendemos.
# Esta tabla servirá para importar datos del "Tarifa Incident" de Diciembre 2018
class Articulo(models.Model):
	codigo = models.CharField(max_length=200)
	descripcion = models.CharField(max_length=200)
	tarifa1 = models.FloatField()
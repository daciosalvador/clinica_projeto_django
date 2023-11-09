from django.contrib import admin
from .models import *

admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Consulta)
from __future__ import unicode_literals
from django.contrib import admin
from .models import Cursomod
from .models import Tipocursomod
from .models import Tipopagomod

admin.site.register(Cursomod)
admin.site.register(Tipocursomod)
admin.site.register(Tipopagomod)


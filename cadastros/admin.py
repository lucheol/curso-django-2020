from django.contrib import admin

# Register your models here.
from cadastros.models import Cidade, Pais, Estado

admin.site.register(Pais)
admin.site.register(Estado)
admin.site.register(Cidade)

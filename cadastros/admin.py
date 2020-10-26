from django.contrib import admin

# Register your models here.
from cadastros.models import Cidade, Pais, Estado

class EstadoInline(admin.TabularInline):
    model = Estado

class PaisAdmin(admin.ModelAdmin):

    fields = ('nome', )
    inlines = [
        EstadoInline
    ]

admin.site.register(Pais, PaisAdmin)
admin.site.register(Estado)
admin.site.register(Cidade)

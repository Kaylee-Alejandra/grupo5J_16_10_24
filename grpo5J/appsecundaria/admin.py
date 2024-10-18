from django.contrib import admin
from .models import AlumnoT, Frase
# Register your models here.



class ComentarioInLine(admin.TabularInline):
    model=Frase
    extra=1

class AlumnoAdmin(admin.ModelAdmin) :
    fields= ["Apaterno", "Amaterno", "fecha_nacimiento", "fecha_ingreso", "nombre"] 
    list_display= ["Apaterno", "Amaterno", "nombre"]
    inlines= [ComentarioInLine]

admin.site.register(AlumnoT, AlumnoAdmin)

@admin.register(Frase)

class FraseAdmin(admin.ModelAdmin):
    fields= ["comentario", "Alumno_fk"]
    list_display= ["comentario"]
from django.shortcuts import render, get_object_or_404
from .models import AlumnoT, Frase


# Create your views here.
def index_vista(request):
    objeto= AlumnoT.objects.all().order_by("id") #nuevo diccionario
    return render(request, "index.html", {"objeto":objeto})

def Alumno_vista(request,id):
    alumno= get_object_or_404(AlumnoT, id=id)
    return render(request, "alumno.html", {'objeto':alumno })

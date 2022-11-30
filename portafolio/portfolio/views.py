from django.shortcuts import render
from .models import Project

# Create your views here.
def portfolio(request):
#    return HttpResponse(html_cabecera + "<h3>Mi Portafolio</h3><p>Mi listado de trabajos realizados</p>")        
    projects = Project.objects.all()    # Obtener un QuerySet y pasarlo a la pagina
    return render(request,'portfolio/portfolio.html',{'projects':projects})

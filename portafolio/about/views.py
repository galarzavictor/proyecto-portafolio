from django.shortcuts import render
from .models import Course, Skill

# Create your views here.
def about(request):
#    return HttpResponse(html_cabecera + "<h3>Acerca de ...</h3><p>Soy Andres y soy programador</p>")    
#    return render(request,'core/about.html')
    courses = Course.objects.all()
    skills = Skill.objects.all()
    return render(request, 'about/about.html', {'courses':courses, 'skills':skills})
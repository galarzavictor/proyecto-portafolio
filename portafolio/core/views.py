from django.shortcuts import render, HttpResponse

html_cabecera ='''
<h1>Mi Portafolio Personal</h1>
<ul>
    <li> <a href="/">Inicio</a> </li>
    <li> <a href="/about-me/">Acerca de</a> </li>    
    <li> <a href="/portfolio/">Portafolio</a> </li>    
    <li> <a href="/contact/">Contacto</a> </li>    
</ul>    
'''
# Create your views here.
def home(request):
#    return HttpResponse(html_cabecera + "<h3>Página Principal</h3>")
    return render(request,'core/home.html')

def contact(request):
#    return HttpResponse(html_cabecera + "<h3>Contacto</h3><p>Ponte en contacto conmigo al numero +591 71550714</p>")            
    return render(request,'core/contact.html')
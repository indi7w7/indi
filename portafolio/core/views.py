from django.shortcuts import render,HttpResponse

# Create your views here.
html_cabecera="""
<h1>Mi portafolio Personal 
<ul>
  <li><a href="/">Inicio</a></li>
  <li><a href="/about-me/"Acerca de</a></li>
  <li><a href="portafolio/">Portafolio</a></li>
  <li><a href="contact/">contact</a></li>
</ul>
"""
 
def home(request):
    return render(request,'core/home.html')

def about(request):
    return render(request,'core/about.html')

def portafolio(request):
    return render(request,'core/portafolio.html') 

def contact(request):
    return render(request,'core/contact.html')       
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'mainapp/index.html',{
        'title':'Inicio | pagina pricipal', 
                                                
    })

def about(request):
    mensaje='Bienvenido mi nombre es:Pablo...'
    return render(request,'mainapp/about.html',{
        'title': 'Acerca de Nosotros', 'content': 'Somos un grupo de desarrolladores de SW multiplataforma', 'mensaje':mensaje

    })

def mision(request):
    return render(request,'mainapp/mision.html',{
        'title_mision':'mision', 
        'content_mision':'.:Bienvenido a la mision de mi empresa:.'
                                                
    })

def vision(request):
    return render(request,'mainapp/vision.html',{
        'title_vision':'mision', 
        'content_vision':'.:Bienvenido a la vision de mi empresa:.'
                                                
    })




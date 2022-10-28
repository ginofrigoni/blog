from django.shortcuts import render


# Create your views here.
def index(request):
    data = {
        'titulo' : 'Titulo este es el',
    }
    return render(request, 'index.html', data)

def ver(request, nombre_del_art):
    data = {
        'titulo' : nombre_del_art,
    }
    return render(request, 'articulo.html', data)

def about(request):
    data = {
        'titulo' : 'about',
    }
    return render(request, 'articulo.html', data)
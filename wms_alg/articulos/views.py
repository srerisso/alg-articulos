from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Articulo

def index(request):
    articulos_list = Articulo.objects.all()
    # Listado de articulos paginados
    page = request.GET.get('page', 1)
    paginator = Paginator(articulos_list, 200)

    try:
        articulos = paginator.page(page)
    except PageNotAnInteger:
        articulos = paginator.page(1)
    except EmptyPage:
        articulos = paginator.page(paginator.num_pages)

    return render(request, 'articulos/index.html', {'articulos' : articulos})

def detail(request, articulo_id):
    return HttpResponse("You're looking at articulo %s." % articulo_id)

def save(request, articulo_id):
    Articulo.save()
    return HttpResponseRedirect(reverse('articulos:results', args=(articulo.id,)))
    # Articulo.save(datos)

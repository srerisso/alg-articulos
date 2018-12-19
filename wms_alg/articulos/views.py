# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Articulo
from .forms import ArticuloForm

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

# guarda function
def guarda(request):
    # Formulario con datos, siempre será POST
    if request.method == 'POST':
        codigo = request.POST['codigo']
        descripcion = request.POST['descripcion']
        tarifa1 = request.POST['tarifa1']

        Articulo.objects.create(
            codigo = codigo,
            descripcion = descripcion,
            tarifa1 = tarifa1
        )

        return HttpResponse('')

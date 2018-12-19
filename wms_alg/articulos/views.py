# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
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

def guarda(request):
    # Formulario con datos, siempre será POST
    a = Articulo.objects.get(pk=1)
    f = ArticuloForm(request.POST, instance=a)
    if form.is_valid():
        form.save()

    # return HttpResponseRedirect(reverse('articulos/index.html', {'form': form}))
    return render(request, 'articulos:index')

from django.shortcuts import render
from .models import Articulo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    articulos_list = Articulo.objects.all()
    # Listado de articulos paginados
    page = request.GET.get('page', 1)
    paginator = Paginator(articulos_list, 100)

    try:
        articulos = paginator.page(page)
    except PageNotAnInteger:
        articulos = paginator.page(1)
    except EmptyPage:
        articulos = paginator.page(paginator.num_pages)

    return render(request, 'articulos/index.html', {'articulos' : articulos})



def detail(request, articulo_id):
    return HttpResponse("You're looking at articulo %s." % articulo_id)

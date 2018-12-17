from django.http import HttpResponse
from django.template import loader
from .models import Articulo

def index(request):
    first100 = Articulo.objects.order_by('descripcion')[:100]
    template = loader.get_template('articulos/index.html')
    context = {
        'first100' : first100,
    }
    # output = ', '.join(art.descripcion for art in first100)
    return HttpResponse(template.render(context, request))
    # Listado de articulos paginados


def detail(request, articulo_id):
    return HttpResponse("You're looking at articulo %s." % articulo_id)

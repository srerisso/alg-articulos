from django.conf.urls import url

from . import views

app_name = 'articulos'
urlpatterns = [
    # /articulos
    url(r'^$', views.index, name='index'),
    # ex: /articulos/5/
    url(r'^(?P<articulo_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /articulos/guarda/
    url(r'^(?P<articulo_id>[0-9]+)/guarda/$', views.guarda, name='guarda'),
]

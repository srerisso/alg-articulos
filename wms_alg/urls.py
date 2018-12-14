from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('articulos/', include('articulos.urls')),
    path('admin/', admin.site.urls),
]

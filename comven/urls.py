from django.conf.urls import url
from .views import CrearCliente, ActualizarCliente, BorrarCliente, ListaCliente, DetailView, IndexView


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^juegos/$', IndexView.as_view(), name='index'),
    url(r'^juegos/(?P<pk>[0-9]+)/$', DetailView.as_view(), name='detail'),
    url(r'^cliente/$', ListaCliente.as_view(), name='cliente'),
    url(r'^cliente/crear/$', CrearCliente.as_view(), name='crear'),
    url(r'^cliente/actualizar/(?P<pk>[0-9]+)/$', ActualizarCliente.as_view(), name='actualizar'),
    url(r'^cliente/borrar/(?P<pk>[0-9]+)/$', BorrarCliente.as_view(), name='borrar'),
]

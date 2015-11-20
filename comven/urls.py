from django.conf.urls import url
from .views import CrearCliente, ActualizarCliente, BorrarCliente, ListaCliente, DetailCliente, DetailView, IndexView, CrearJuego, ActualizarJuego, BorrarJuego
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^juego/$', IndexView.as_view(), name='index2'),
    url(r'^juego/(?P<pk>[0-9]+)/$', DetailView.as_view(), name='detail'),
    url(r'^juego/crear/$', CrearJuego.as_view(), name='crear1'),
    url(r'^juego/(?P<pk>[0-9]+)/actualizar/$', ActualizarJuego.as_view(), name='actualizar1'),
    url(r'^juego/(?P<pk>[0-9]+)/borrar/$', BorrarJuego.as_view(), name='borrar1'),
    url(r'^cliente/$', ListaCliente.as_view(), name='cliente'),
    url(r'^cliente/(?P<pk>[0-9]+)/$', DetailCliente.as_view(), name='detail_cliente'),
    url(r'^cliente/crear/$', login_required(CrearCliente.as_view()), name='crear2'),
    url(r'^cliente/(?P<pk>[0-9]+)/actualizar/$', login_required(ActualizarCliente.as_view()), name='actualizar2'),
    url(r'^cliente(?P<pk>[0-9]+)/borrar/$', login_required(BorrarCliente.as_view()), name='borrar2'),
]

from django.conf.urls import url
from . import views
from .views import Crearcliente, Actualizarcliente, Borrarcliente, Registro


urlpatterns = [
    url(r'^$', views.Registro.as_view(), name='lista'),
#   url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^crear/$', Crearcliente.as_view(), name='crear'),
    url(r'^(?P<pk>[0-9]+)/$', Actualizarcliente.as_view(), name='actualizar'),
    url(r'(?P<pk>[0-9]+)/borrar/$', Borrarcliente.as_view(), name='borrar'),
]

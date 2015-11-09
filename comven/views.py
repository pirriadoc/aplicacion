from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django.core.context_processors import csrf
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView,ListView

from .forms import Registro
from .models import Juego, Cliente, Empresa

# Create your views here.

#vistas al modo tradicional
#def index(request):
#    juego = Juego.objects.order_by('-titulo')[:5]
#    context = {'juego': juego}
#    return render(request, 'comven/index.html', context)
#def detail(request, Juego_id):
#    juego = get_object_or_404(Juego, pk=Juego_id)
#    return render(request, 'comven/detail.html', {'juego': juego})
#vistas genericas
class IndexView(generic.ListView):
    template_name='comven/index.html'
    context_object_name='juego'
    def get_queryset(self):
        return Juego.objects.order_by('titulo')[:7]
class DetailView(generic.DetailView):
    template_name='comven/detail.html'
    model = Juego
    fields = ['titulo']
#Vista de registro
class Registro(generic.ListView):
    template_name = "comven/registro.html"
    model = Cliente
    context_object_name='registro'
#Vistas basadas en clases para los registros
class Crearcliente(CreateView):
    model = Cliente
    fields = ['nombre', 'direccion']
    success_url = '/'
#    def form_valid(self, form):
#        print 'save'
#        form.save()
class Actualizarcliente(UpdateView):
    model = Cliente
    fields = ['nombre', 'direccion']
    success_url = '/'
class Borrarcliente(DeleteView):
    model = Cliente
    success_url = '/'
#vistas genericas

#class IndexView(generic.ListView):
#    template_name = 'comven/index.html'
#    context_name = 'juego'

#    def get_queryset(self):
#        """Return the last five published questions."""
#        return Juego.objects.order_by('-titulo')[:5]

#class DetailView(generic.DetailView):
#    model = Juego
#    template_name = 'comven/index.html'

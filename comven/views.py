from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django.core.context_processors import csrf
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView,ListView
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import LoginForm
from .models import Juego, Cliente, Empresa

# Create your views here.

# Clase para poder usar el decorador login_required con clases.
# class LoginRequiredMixin(object):
#   @classmethod
#    def as_view(cls, **initkwargs):
#        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
#        return login_required(view)
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
#Vista de Cliente
class ListaCliente(generic.ListView):
    template_name = "comven/cliente.html"
    model = Cliente
    context_object_name='cliente'

#Vistas basadas en clases para los clientes

class CrearCliente(CreateView):
    model = Cliente
    fields = ['nombre','direccion']
    success_url = '/'
#    def form_valid(self, form):
#        print 'save'
#        form.save()

class ActualizarCliente(UpdateView):
    model = Cliente
    fields = ['nombre', 'direccion']
    success_url = '/'

class BorrarCliente(DeleteView):
    model = Cliente
    success_url = '/'
#Vistas basadas en clases para los juegos
class CrearJuego(CreateView):
    model = Juego
    fields = ['titulo', 'empresa', 'genero', 'plataforma', 'descripcion', 'cantidad']
    success_url = '/'
#    def form_valid(self, form):
#        print 'save'
#        form.save()
class ActualizarJuego(UpdateView):
    model = Juego
    fields = ['titulo', 'empresa', 'genero', 'plataforma', 'descripcion', 'cantidad']
    success_url = '/'
class BorrarJuego(DeleteView):
    model = Juego
    success_url = '/'
#Vistas para login y logout
def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            success_url = '/'
        else:
            messages.error(request, 'Account not available.')
    else:
         messages.error(request, 'Password incorrect or account not available.')
    return HttpResponseRedirect ('/')

def logout_view(request):
    logout(request)
    success_url='/'




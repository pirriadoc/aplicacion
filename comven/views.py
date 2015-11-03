from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic
from django.core.context_processors import csrf

from .forms import Registro
from .models import Juego, Cliente, Empresa
# Create your views here.

#vistas al modo tradicional
def index(request):
    juego = Juego.objects.order_by('-titulo')[:5]
    context = {'juego': juego}
    return render(request, 'comven/index.html', context)
def detail(request, Juego_id):
    juego = get_object_or_404(Juego, pk=Juego_id)
    return render(request, 'comven/detail.html', {'juego': juego})
def registro(request):
    form = Registro()
    return render(request, 'comven/registro.html', {'form': form})

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

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Juego
# Create your views here.

def index(request):
    juego = Juego.objects.order_by('-titulo')[:5]
    context = {'juego': juego}
    return render(request, 'comven/index.html', context)
def detail(request, Juego_id):
    juego = get_object_or_404(Juego, pk=Juego_id)
    return render(request, 'comven/detail.html', {'juego': juego})

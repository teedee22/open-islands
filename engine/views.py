from django.shortcuts import render
from engine.models import Building, Player
from django.http import HttpResponse
# Create your views here.

def index(request):
    buildings = Building.objects.all()
    player = Player.objects.get(pk=1)
    return render(request, 'engine/index.html', {"player": player, "buildings": buildings})

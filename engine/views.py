from django.shortcuts import render
from engine.models import Building, Player
from django.http import HttpResponse

from django.utils import timezone
import time
# Create your views here.

def index(request):
    buildings = Building.objects.all()
    player = Player.objects.get(pk=1)
    seconds_passed = (timezone.now() - player.last_action).total_seconds()
    player.last_action = timezone.now()
    player.save()
    return render(request, 'engine/index.html', {"player": player, "buildings": buildings, "seconds_passed": seconds_passed})

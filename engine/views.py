from django.shortcuts import render
from engine.models import Building, Player, Goldmine
from django.http import HttpResponse

from django.utils import timezone
import time
# Create your views here.

def index(request):
    buildings = Building.objects.all()
    player = Player.objects.get(pk=1)
    seconds_passed = (timezone.now() - player.last_action).total_seconds()
    player.gold += (seconds_passed / 3600) * player.gold_accrual
    player.lumber += (seconds_passed / 3600) * player.lumber_accrual
    player.stone += (seconds_passed / 3600) * player.stone_accrual
    player.last_action = timezone.now()
    player.save()
    return render(request, 'engine/index.html', {"player": player,
                                                 "buildings": buildings,
                                                 "seconds_passed": seconds_passed})

def make(request):
    dummy = Goldmine(name="dummy")
    for mine in range(5):
        building = Goldmine(name=f'Goldmine level {mine}')
        building.level = mine
        building.cost_gold = building.calc_cost_gold()
        building.cost_lumber = building.calc_cost_lumber()
        building.cost_stone = building.calc_cost_stone()
        building.gold_per_hour = building.output()
        building.score_addition = building.calc_score_addition()
        building.save()

# def add_building(request):

from django.contrib import admin

from .models import Building, Player, Goldmine
# Register your models here.

admin.site.register(Building)
admin.site.register(Player)
admin.site.register(Goldmine)

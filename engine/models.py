from django.db import models


class Player(models.Model):
    id = models.IntegerField # Maybe rehash as a foreign key of User object
    gold = models.IntegerField(default=200)
    lumber = models.IntegerField(default=200)
    stone = models.IntegerField(default=200)
    score = models.IntegerField(default=1)
    last_action = models.DateTimeField(auto_now=False)

    def __str__(self):
        return f'{self.id} Gold: {self.gold} Lumber: {self.lumber} Stone: {self.stone} Score: {self.score}'


class Building(models.Model):
    name = models.CharField(max_length=64)
    max_level = models.IntegerField(default=20)
    level = models.IntegerField(default=0)
    cost = models.IntegerField(default=13)

    def output(self):
        if self.level > 0:
            return 13 * self.level
        else:
            return 13

    def cost_gold(self):
        if self.level > 0:
            return 50 * self.level
        else:
            return 50

    def __str__(self):
        return f'{self.name} ({self.level})'

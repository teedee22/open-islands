from django.db import models


class Building(models.Model):
    name = models.CharField(max_length=64)
    max_level = models.IntegerField(default=20)
    level = models.IntegerField(default=0)
    cost_gold = models.IntegerField(default=13)
    cost_lumber = models.IntegerField(default=0)
    cost_stone = models.IntegerField(default=0)
    score_addition = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name} ({self.level})'


def costs(level, multiplier):
    if level > 0:
        return multiplier * 2 ** level
    else:
        return multiplier / 2


class Goldmine(Building):
    gold_per_hour = models.IntegerField(default=0)

    def output(self):
        return costs(self.level, 13)

    def calc_cost_gold(self):
        return costs(self.level, 40)

    def calc_cost_lumber(self):
        return costs(self.level, 70)

    def calc_cost_stone(self):
        return costs(self.level, 60)

    def calc_score_addition(self):
        return costs(self.level, 2)


class Player(models.Model):  # Maybe this should be an island ID
    id = models.IntegerField  # Maybe rehash as a foreign key of User object
    score = models.IntegerField(default=1)
    last_action = models.DateTimeField(auto_now=False)

    # Resources
    gold = models.FloatField(default=200)
    gold_accrual = models.IntegerField(default=3)
    lumber = models.FloatField(default=200)
    lumber_accrual = models.IntegerField(default=4)
    stone = models.FloatField(default=200)
    stone_accrual = models.IntegerField(default=4)

    # Attributes
    buildings = models.ManyToManyField(Building, blank=True)

    def __str__(self):
        return f'{self.id} Gold: {self.gold} Lumber: {self.lumber} \
                  Stone: {self.stone} Score: {self.score}'

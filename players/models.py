from django.db import models
import random


class Player(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    password = models.IntegerField()

    def save(self, *args, **kwargs):
        print("-------------------------------2")
        pwd = random.randint(1000, 9999)
        self.password = pwd
        super(Player, self).save(*args, **kwargs)
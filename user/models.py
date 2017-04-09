from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Location(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    info = models.TextField(null=True)

    def dict(self):
        return {"x": self.x,
                "y": self.y}


class UserInfo(models.Model):
    user = models.OneToOneField(User, related_name="info")
    points = models.IntegerField(default=100)
    location = models.ForeignKey(Location, null=True, related_name="user")


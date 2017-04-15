from django.db import models
from django.contrib.auth.models import User
from user.models import Location


class Job(models.Model):
    allTypes = ((0, "Прогулянка із псом"),
                (1, "Похід за продуктами"),
                (2, "Миття вікон"),
                (3, "Ремонт меблів"),
                (4, "Супровід дитини у школу"),
                (5, "Ремонт одягу"),
                (6, "Миття машини"),
                (7, "Послуги няні"),
                (8, "Ремонт велосипеду"),
                (9, "Догляд за домашньою твариною на певний час"),
                (10, "Допомога з перевезенням речей"),
                (11, "Фарбування паркану"),
                (12, "Прибирання квартири"),
                (13, "Миття посуду"),
                )
    points = models.IntegerField()
    description = models.TextField(null=True)
    type = models.IntegerField(choices=allTypes)
    deadline = models.DateField()
    customer = models.ForeignKey(User, related_name="jobs")
    performer = models.ForeignKey(User, related_name="todo", null=True)
    location = models.ForeignKey(Location, related_name="job", null=True)

    def dict(self):
        return {"points": self.points,
                "description": self.description,
                "type": self.type,
                "deadline": self.deadline.__str__(),
                "customer": self.customer.__str__(),
                "performer": self.performer.__str__(),
                "location": self.location.dict()}



# Create your models here.

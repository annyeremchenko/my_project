from django.db import models
from django.contrib.auth.models import User
from user.models import Location


class Job(models.Model):
    points = models.IntegerField()
    description = models.TextField(null=True)
    type = models.IntegerField()
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

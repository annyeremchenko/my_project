from django.shortcuts import render
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Job
from django.shortcuts import HttpResponse
import math, json


class JobSearch(View):
    @method_decorator(login_required(login_url='/login/'))
    def get(self, request):
        location = request.user.info.location
        delta_lat = 0.1
        delta_lng = delta_lat / math.cos(math.radians(location.y))
        jobs = Job.objects.filter(location__x__lte=location.x + delta_lng,
                           location__x__gte=location.x - delta_lng,
                           location__y__lte=location.y + delta_lat,
                           location__y__gte=location.y - delta_lat)
        print([i.dict() for i in jobs])
        return HttpResponse(json.dumps([i.dict() for i in jobs], indent=4, sort_keys=True), content_type='application/json')

# Create your views here.

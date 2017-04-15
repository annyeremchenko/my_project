from django.shortcuts import render
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Job
from django.shortcuts import HttpResponse
from django.db.models import Q
import math, json


class JobSearch(View):
    @method_decorator(login_required(login_url='/login/'))
    def get(self, request):
        location = request.user.info.location
        delta_lat = 0.1
        delta_lng = delta_lat / math.cos(math.radians(location.y))
        jobs = Job.objects.filter(~Q(customer=request.user),
                                  performer=None,
                                  location__x__lte=location.x + delta_lng,
                                  location__x__gte=location.x - delta_lng,
                                  location__y__lte=location.y + delta_lat,
                                  location__y__gte=location.y - delta_lat)
        #return HttpResponse(json.dumps([i.dict() for i in jobs], indent=4, sort_keys=True), content_type='application/json')
        return render(request, "mapJobs.html", {'jobs': jobs})

    @method_decorator(login_required(login_url='/login/'))
    def post(self, request):
        if (request.POST.__contains__('id')):
            id = int(request.POST['id'])
            job = Job.objects.get(id=id)
            print (job.dict())
            if (job.performer is not None):
                return HttpResponse(json.dumps({"status": "occupied"}), content_type='application/json')
            job.performer = request.user
            job.save()
            return HttpResponse(json.dumps({"status": "ok"}), content_type='application/json')
        return HttpResponse(json.dumps({"status": "error key"}), content_type='application/json')

class JobAll(View):
    @method_decorator(login_required(login_url='/login/'))
    def get(self, request):
        jobs = Job.objects.all()
        return render(request, "mapJobs.html", {'jobs': jobs})


class Map(View):
    @method_decorator(login_required(login_url='/login/'))
    def get(self, request):
        location = {}
        if (request.GET.__contains__('lat') and request.GET.__contains__('lng')):
            location = {'lat': request.GET['lat'],
                        'lng': request.GET['lng']}
        return render(request, "map.html", location)

# Create your views here.

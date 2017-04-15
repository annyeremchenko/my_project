from django.shortcuts import render
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect
from job.models import Job, Location
from .models import UserInfo
from django.shortcuts import HttpResponse
import sys, json, math


class Home(View):
    @method_decorator(login_required(login_url='/login/'))
    def get(self, request, **params):
        return render(request, "home.html", params)

    @method_decorator(login_required(login_url='/login/'))
    def post(self, request):
        print(request.POST)
        if request.POST.__contains__('key') and request.POST.__contains__('value'):
            key = request.POST['key']
            val = request.POST['value']
            if key == 'firstname':
                request.user.first_name = val
                request.user.save()
                return HttpResponse(json.dumps({"status": "ok"}), content_type='application/json')
            elif key == 'lastname':
                request.user.last_name = val
                request.user.save()
                return HttpResponse(json.dumps({"status": "ok"}), content_type='application/json')
            else:
                return HttpResponse(json.dumps({"status": "error key"}), content_type='application/json')
        elif request.POST.__contains__('type') and request.POST.__contains__('points') and request.POST.__contains__('description') and request.POST.__contains__('deadline') and request.POST.__contains__('lng') and request.POST.__contains__('lat'):
            job_type = int(request.POST['type'])
            points = int(request.POST['points'])
            description = request.POST['description']
            deadline = request.POST['deadline']
            lng = float(request.POST['lng'])
            lat = float(request.POST['lat'])
            if request.user.info.points < points:
                return self.get(request, error='Not enough points to post job')
            location = Location.objects.create(x=lng, y=lat)
            Job.objects.create(type=job_type,
                               points=points,
                               description=description,
                               deadline=deadline,
                               customer=request.user,
                               location=location)
            request.user.info.points -= points
            request.user.info.save()
            request.method = 'get'  # виправлення багу із повторним надсиланням форми
            return redirect('/home/')
        else:
            return HttpResponse(json.dumps({"status": "error request"}), content_type='application/json')


class Signup(View):
    def get(self, request, params={}):
        return render(request, "signup.html", params)

    def post(self, request):
        params = request.POST
        try:
            try:
                user = User.objects.get(username=params['username'])
                if user is not None:
                    self.get(request, {'error': 'Error, we already have a user with such name'})
            except:
                print(params)
                try:
                    print(params['email'])
                    user = User.objects.get(email=params['email'])
                    if user is not None:
                        self.get(request, {'error': 'Error, we already have a user with such email'})
                except:
                    print(sys.exc_info())
                    print('success')
            if params['password'] != params['password_repeat']:
                return render(request, 'auth.html', {'error': "Passwords don't matches"})
            user = User.objects.create_user(params['username'], params['email'], params['password'])
            user.last_name = params['lastname']
            user.first_name = params['firstname']
            lat = float(params['lat'])
            lng = float(params['lng'])
            user.save()
            location = Location.objects.create(x=lng, y=lat)
            UserInfo.objects.create(location=location, user=user)


            user = authenticate(username=params['username'], password=params['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if request.GET.__contains__('next'):
                        return redirect(request.GET['next'])
                    else:
                        return redirect('/home/')
                else:
                    self.get(request, {'error': 'Some error'})
            else:
                self.get(request, {'error': 'Some error'})
            login(request, user)
            return redirect('/home/')
        except ValueError:
            self.get(request, {'error': 'Some error on server'})


class Login(View):
    def get(self, request, params={}):
        return render(request, "login.html", params)

    def post(self, request):
        params = request.POST
        if params['email'].find('@') == -1:
            username = params['email']
        else:
            try:
                username = User.objects.get(email=params['email'])
            except:
                print('error')
                return self.get(request,  {'login': "password don't match"})
        user = authenticate(username=username, password=params['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                try:
                    print(request.GET['next'])
                    return redirect(request.GET['next'])
                except:
                    return redirect('/home/')
            else:
                return self.get(request, {'login': 'error disabled'})
        else:
            return self.get(request, {'login': "password don't match"})


class Logout(View):
    @method_decorator(login_required(login_url='/login/'))
    def get(self, request):
        logout(request)
        return redirect("/login/")

# Create your views here.

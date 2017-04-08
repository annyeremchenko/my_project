from django.shortcuts import render
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect
import sys


class Home(View):
    @method_decorator(login_required(login_url='/login/'))
    def get(self, request):
        return render(request, "home.html", {})


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
            user.save()
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
        return redirect("/login/")

# Create your views here.

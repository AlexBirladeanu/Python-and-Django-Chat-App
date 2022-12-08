from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from aso_app.models import Thread, User


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            add_threads(user)
            return redirect('/')
        else:
            return redirect('/members/login')
    else:
        return render(request, 'authentication/login.html', {})


def logout_user(request):
    logout(request)
    return redirect('/members/login')


def add_threads(active_user):
    active_threads = Thread.objects.filter(first_person=active_user) | Thread.objects.filter(second_person=active_user)
    all_users = User.objects.exclude(id=active_user.id)
    for user in all_users:
        thread_already_exists = False
        for thread in active_threads:
            if thread.second_person == user:
                thread_already_exists = True
            if thread.first_person == user:
                thread_already_exists = True
        if not thread_already_exists:
            Thread.objects.create(first_person=active_user, second_person=user)




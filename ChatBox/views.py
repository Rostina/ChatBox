from django.shortcuts import render

from chat import models


def home(request):
    nerd = request.user
    user = models.Profile.objects.get(email=nerd.email)
    user_list = user.friends.split(',')
    num = str(2)

    return render(request, 'home.html', {'two': num, 'user': user})
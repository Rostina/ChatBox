from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from ChatBox import forms
from chat import models


def home(request):
    """main page"""
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('chat:chat'))
    else:
        return HttpResponseRedirect(reverse('login'))

def contact_us(request):
    form = forms.MessageForm(request.POST or None)
    if form.is_valid():
        admin = models.Profile.objects.get(username="ChatBox staff")
        if request.user.is_authenticated and request.user.is_staff == False:
            user = models.Profile.objects.get(username=request.user.username)
        else:
            user = models.Profile.objects.get(username="No One")
        message = form.save(commit=False)
        message.from_user = user
        message.to_user = admin
        message.save()
        messages.success(request, "Message was recieved by our staff. We will contact you soon")
        if request.user.is_authenticated and request.user.is_staff == False:
            models.FriendMessage.objects.create(
                to_user=user,
                from_user=admin,
                title="We got your " + message.title + " message. We will contact you soon addressing your message."
            )
        return HttpResponseRedirect(reverse('home'))
    return render(request, "contact-us.html", {'form': form})


def loginer(request):
    """logs in user"""
    form = forms.LoginForm()
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.add_message(request, messages.SUCCESS, "Login Sucessfull!")
                    return HttpResponseRedirect(reverse('home'))
                else:
                    messages.add_message(request, messages.ERROR, "This account has been disabled sorry!")
                    return HttpResponseRedirect(reverse('home'))
            else:
                messages.add_message(request, messages.ERROR, "Invalid Login!")
    return render(request, 'login.html', {'form': form})


@login_required()
def admin_sign_up(request):
    pass


def sign_up(request):
    """ User could sign up to chat and make account"""
    form = forms.ProfileForm()
    if request.method == "POST":
        form = forms.ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.picture = form.cleaned_data['picture']
            profile.username = form.cleaned_data['first_name'] + " " + form.cleaned_data['last_name']
            profile.save()

            user = User.objects.create_user(
                username=profile.username,
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            login(request, user)
            new_user = models.Profile.objects.get(username=request.user.username)
            new_user.friends = str(new_user.pk)
            new_user.save()
            messages.success(request, "You are all signed up")

    return render(request, 'profile_form.html', {"form": form})

"""
class SignUpView(CreateView):
    fields = ("first_name", "last_name", "phone",
              "email", "birthday", "gender", "picture"
              )
    model = models.Profile

    def form_valid(self, form):
        User.objects.create_user(
            username = "{} {}".format(
                form.cleaned_data['first_name'],
                form.cleaned_data['last_name']
            ),
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
"""

def logout_view(request):
    """logs out user"""
    logout(request)
    messages.add_message(request, messages.SUCCESS, "Logout Successfully!")
    return HttpResponseRedirect(reverse('home'))


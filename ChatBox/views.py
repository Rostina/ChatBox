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
    if request.user.is_staff:
        return HttpResponseRedirect(reverse('chat:chat'))
    if request.user.is_authenticated:
        user = models.Profile.objects.get(username=request.user.username)
        friends = user.friends.split(",")
        if len(friends) <= 1:
            return HttpResponseRedirect(reverse('chat:find_friends'))
        return HttpResponseRedirect(reverse('chat:chat'))
    else:
        return HttpResponseRedirect(reverse('login'))


def contact_us(request):
    form = forms.ContactStaffForm(request.POST or None)
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
        messages.success(request, "Message was received by our staff. We will contact you soon")
        if request.user.is_authenticated and request.user.is_staff == False:
            models.FriendMessage.objects.create(
                to_user=user,
                from_user=admin,
                title="We got your " + message.title + " message. We will contact you soon addressing your message."
            )
        return HttpResponseRedirect(reverse('home'))
    return render(request, "contact-us.html", {'form': form, 'message_type': 'contact_us'})


@login_required()
def respond(request):
    form = forms.RespondForm(request.POST or None)
    pk = request.GET.get('pk')
    # if not send_to:
    #     return HttpResponseRedirect(reverse("chat:messages"))
    send_to = models.Profile.objects.get(username=pk)
    if form.is_valid():
        if request.user.is_staff:
            user = models.Profile.objects.get(username="ChatBox staff")
        else:
            user =  models.Profile.objects.get(username=request.user.username)

        message =  form.save(commit=False)
        message.to_user = send_to
        message.from_user = user
        message.save()
        messages.success(request, "Message sent")
        return HttpResponseRedirect(reverse('chat:messages'))
    return render(request, 'contact-us.html', {'form': form, 'message_type': "response"})


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
            return HttpResponseRedirect(reverse('chat:find_friends'))
    return render(request, 'profile_form.html', {"form": form})


def logout_view(request):
    """logs out user"""
    logout(request)
    messages.add_message(request, messages.SUCCESS, "Logout Successfully!")
    return HttpResponseRedirect(reverse('home'))


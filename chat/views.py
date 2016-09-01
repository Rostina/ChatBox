from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views.generic import DetailView

from chat import models, forms


def friend_list(user):
    friends_list = user.friends.split(',')
    friends = [int(x) for x in friends_list]
    return friends


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
                    messages.add_message(request, messages.SUCCESS, "You are now login!")
                    return HttpResponseRedirect(reverse('home'))
                else:
                    messages.add_message(request, messages.ERROR, "This account has been disabled sorry!")
                    return HttpResponseRedirect(reverse('home'))
        else:
            messages.add_message(request, messages.ERROR, "Invalid Login!")
    return render(request, 'chat/login.html', {'form': form})


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
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            login(request, user)
            messages.success(request, "You are all signed up")

    return render(request, 'chat/profile_form.html', {"form": form})

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


class ProfileDetailView(DetailView):
    model = models.Profile


@login_required
def friends(request):
    user = models.Profile.objects.get(username=request.user.username)
    friends = models.Profile.objects.filter(pk__in=friend_list(user))
    return render(request, 'chat/friends.html', {'friends': friends})


@login_required
def find_friends(request):
    friends = models.Profile.objects.all()
    search = request.GET.get("q")
    if search:
        friends = models.Profile.objects.filter(username__icontains=search)
    return render(request, "chat/find_friends.html", {'friends': friends})


@login_required()
def request_friend(request, pk):
    """request friends"""
    user = models.Profile.objects.get(email=request.user.email, username=request.user.username)
    to = models.Profile.objects.get(pk=pk)
    models.FriendMessage.objects.create(
        from_user=user.username,
        to_user=to,
        title="Friend Request"
    )
    messages.success(request, "Friend Request sent!")
    return HttpResponseRedirect(reverse('home'))


@login_required
def confirm_friend(request, pk):
    """confirm friend request"""
    user = request.user
    you = models.Profile.objects.get(username=user.username)
    message = models.FriendMessage.objects.get(pk=pk)
    friend = models.Profile.objects.get(username=message.from_user)
    you.friends = "{},{}".format(you.friends, friend.pk)
    friend.friends = "{},{}".format(friend.friends, you.pk)
    you.save()
    friend.save()
    message.delete(keep_parents=True)
    models.FriendMessage.objects.create(
        from_user=you.username,
        to_user=friend,
        title="Friend Accepted"
    )
    messages.success(request, "Friend Accepted!")
    return HttpResponseRedirect(reverse('chat:messages'))


@login_required()
def message_seen(request, pk):
    """deletes message """
    user = request.user
    message = models.FriendMessage.objects.get(pk=pk)
    if message.to_user.username != user.username:
        messages.error(request, "YOU cant delete this message its not for you")
    else:
        message.delete(keep_parents=True)
        messages.success(request, "messages marked as seen adn deleted")
    return HttpResponseRedirect(reverse('chat:messages'))



@login_required()
def messages_list(request):
    user = models.Profile.objects.get(username=request.user.username)
    messages = models.FriendMessage.objects.filter(to_user=user.pk)
    return render(request, 'chat/messages.html', {'messages': messages})


@login_required()
def post_chat(request):
    user = models.Profile.objects.get(username=request.user.username)
    form = forms.ChatPostForm()
    if request.method == "POST":
        form = forms.ChatPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = user
            post.save()
            messages.success(request, "New ChatBox posted")
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'chat/post_chat.html', {'form': form})


@login_required()
def make_comments(request, pk):
    user = models.Profile.objects.get(username=request.user.username)
    post = get_object_or_404(models.Chat, pk=pk)
    form = forms.CommentForm()
    if request.method == "POST":
        form = forms.CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = user
            comment.share = "Public"
            comment.comment = post
            comment.distance_from_sourse = post.distance_from_sourse + 1
            comment.save()
            messages.success(request, "Comment added")
            return HttpResponseRedirect(reverse('home'))



@login_required()
def post_comment(request, pk):
    user = models.Profile.objects.get(username=request.user.username)
    post = get_object_or_404(models.Chat, pk=pk)
    form = forms.CommentForm(request.POST, request.FILES)
    # image = request.GET.get("image")
    # text = request.GET.get("text")
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = user
        comment.share = "Public"
        comment.comment = post
        comment.distance_from_sourse = post.distance_from_sourse + 1
        comment.save()
        """models.Chat.objects.create(
            comment=post,
            distance_from_sourse=post.distance_from_sourse + 1,
            image=image,
            text=text,
            share="Public",
            user=user,
        )"""
        messages.success(request, "Comment has been added")
    else:
        messages.error(request, "Comment need either a picture or a comment")
    return HttpResponseRedirect(reverse('home'))



@login_required()
def chat_box_posts(request):
    user = models.Profile.objects.get(username=request.user.username)
    friends = friend_list(user)
    posts_list = models.Chat.objects.filter(distance_from_sourse=1).order_by("-time_posted")
    paginator = Paginator(posts_list, 40) # Show 5 contacts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    return render(request, 'chat/chatbox.html', {'user': user, 'friends': friends, 'posts': posts})






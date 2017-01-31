from django import template

from chat import models

register = template.Library()


@register.assignment_tag()
def post_filter(post, user, friends):
    if friends == "admin":
        return True
    elif post.share == 'Public' or post.user == user:
        return True
    elif friends == False:
        return False
    if post.share == "Only Me":
        if user == post.user:
            return True
        else:
            return False
    elif post.share == "Private Message":
        if user == post.private_message:
            return True
        return False
    for sharer in post.users.all():
        if sharer.id in friends:
            return True

    if post.user.pk in friends:
        return True
    else:
        return False


@register.assignment_tag()
def share_button_filter(post, user):
    if post.share == 'Public' or post.user == user:
        return False
    for sharer in post.users.all():
        if sharer == user:
            return False
    return True

@register.assignment_tag()
def last_5_comments(comments, loop):
    length = len(comments) - 5
    # loop = int(loop) + 1
    if length < 0:
        return comments
    return comments[length:]


@register.assignment_tag()
def new_distance(distance):
    return distance + 1


@register.assignment_tag()
def has_comments(post, distance):
    comments = models.Chat.objects.filter(comment=post).filter(distance_from_sourse=distance).order_by("-time_posted")
    return comments


@register.assignment_tag()
def who_sent_messages(private_messages):
    messages_from = {}
    time = ""
    add = True
    for message in private_messages:
        username = message.user.username
        if time != message.user:
            try:
                time = models.Chat.objects.filter(private_message=message.user, user=message.private_message).latest('time_posted')
                add = False
            except:
                add = True
            print("TIME: " + time.text)
        if message.time_posted > time.time_posted and add is False:

            if username in messages_from:
                messages_from[username] += 1
            else:
                messages_from[username] = 1
        elif add is True:
            if username in messages_from:
                messages_from[username] += 1
            else:
                messages_from[username] = 1
        else:
            messages_from[username] = 0

    return messages_from


@register.inclusion_tag('chat/comment_loop.html')
def comments_list(comments):
    return {'comments': comments}


"""

for num in numbers:
    if num:
        lop(n)

def lop(numbers):
    for num in numbers:
        print("YESSSSSSSSS")
        if n:
            lop(n)"""

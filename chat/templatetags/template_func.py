from django import template

from chat import models

register = template.Library()


@register.assignment_tag()
def post_filter(post, user, friends):
    for sharer in post.users.all():
        if sharer.id in friends:
            return True
    if post.share == 'Public' or post.user == user:
        return True
    elif friends == False:
        return False
    elif post.user.pk in friends:
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
def new_distance(distance):
    return distance + 1


@register.assignment_tag()
def has_comments(post, distance):
    comments = models.Chat.objects.filter(comment=post).filter(distance_from_sourse=distance)
    return comments


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

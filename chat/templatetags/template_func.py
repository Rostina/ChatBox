from django import template

register = template.Library()

@register.assignment_tag()
def post_filter(post, user, friends):
    if post.share == 'Public' or post.user == user:
        return True
    elif post.user.pk in friends:
        return True
    else:
        return False


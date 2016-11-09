from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, validate_comma_separated_integer_list
from django.db import models

# Create your models here.



class Profile(models.Model):
    GENDERCHOICES = (("Male", "Male"), ("Female", "Female"))

    picture = models.ImageField(upload_to='images', default='nick.jpg')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=105)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone Number")
    phone = models.CharField(max_length=17, validators=[phone_regex])
    email = models.EmailField(max_length=150)
    birthday = models.DateTimeField()
    gender = models.CharField(max_length=6, choices=GENDERCHOICES)
    friends = models.CharField(
        max_length=100000,
        default="",
        validators=[validate_comma_separated_integer_list]
    )
    firends2 = models.ManyToManyField("Profile", null=True, blank=True)


    """def friend_list(self):
        return list(self.friends.all())"""

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class FriendMessage(models.Model):
    from_user = models.CharField(max_length=105)
    to_user = models.ForeignKey(Profile)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Chat(models.Model):
    SHARINGCHOICES = (("Public", "Public"), ("Friends", "Friends"))
    comment = models.ForeignKey('self', null=True, blank=True, default=None)
    distance_from_sourse = models.PositiveIntegerField(default=1)
    title = models.CharField(max_length=125, default="Post", null=True, blank=True)
    image = models.ImageField(upload_to='images',
                              null=True, blank=True)
    text =  models.TextField(null=True, blank=True)
    share = models.CharField(max_length=50, choices=SHARINGCHOICES)
    user = models.ForeignKey(Profile)
    time_posted = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        if self.title == "Post":
            if self.text:
                return "Text: {}".format(self.text)
            else:
                return "pk: {}".format(self.pk)
        return self.title

    def clean(self):
        if self.comment == self:
            raise ValidationError("a chat cant be a comment on its self")








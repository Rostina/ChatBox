from django.contrib import admin

# Register your models here.
from chat import models

admin.site.register(models.Profile)
admin.site.register(models.FriendMessage)
admin.site.register(models.Chat)

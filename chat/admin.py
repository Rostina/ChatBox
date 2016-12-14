from django.contrib import admin

# Register your models here.
from chat import models

class ChatAdmin(admin.ModelAdmin):
    search_fields = ['distance_from_sourse', 'amount_likes', 'pk', 'text', 'title']
    list_filter = ['distance_from_sourse', 'amount_likes']

    class Meta:
        model = models.Chat


admin.site.register(models.Profile)
admin.site.register(models.FriendMessage)
admin.site.register(models.Chat, ChatAdmin)


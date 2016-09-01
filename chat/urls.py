from django.conf.urls import url

from chat import views

urlpatterns = [
    url(r'^$', views.chat_box_posts, name='chat'),
    url(r'sign up/$', views.sign_up, name="sign_up"),
    url(r'login/$', views.loginer, name="login"),
    url(r'logout/$', views.logout_view, name="logout"),

    url(r'^friends/$', views.friends, name='friends'),
    url(r'^find friends/$', views.find_friends, name='find_friends'),
    url(r'^find friends/(?P<pk>\d+)/$', views.ProfileDetailView.as_view(), name='friend_detail'),
    url(r'^friend request/(?P<pk>\d+)/$', views.request_friend, name="friend_request"),
    url(r'^friend accepted/(?P<pk>\d+)/$', views.confirm_friend, name='confirm_friend'),

    url(r'^messages/$', views.messages_list, name="messages"),
    url(r'^message seen/(?P<pk>\d+)/$', views.message_seen, name='message_seen'),

    url(r'^post/$', views.post_chat, name='post'),
    url(r'^post/(?P<pk>\d+)/$', views.make_comments, name='comment'),
    url(r'^comment/(?P<pk>\d+)$', views.post_comment, name='post_comment'),
]
from django.conf.urls import url

from chat import views

urlpatterns = [
    url(r'sign up/$', views.sign_up, name="sign_up"),
    url(r'login/$', views.loginer, name="login"),
    url(r'logout/$', views.logout_view, name="logout"),
    url(r'^find friends/(?P<pk>\d+)/$', views.ProfileDetailView.as_view(), name='friend_detail'),
    url(r'^friend request/(?P<pk>\d+)/$', views.request_friend, name="friend_request"),
    url(r'^friend accepted/(?P<pk>\d+)/$', views.confirm_friend, name='confirm_friend'),
    url(r'^messages/$', views.messages_list, name="messages")
]
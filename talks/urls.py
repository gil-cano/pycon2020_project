from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.track_list, name='list'),
    # url(r'(?P<pk>\d+)/$', views.talk_details),
    url(r'(?P<pk>\d+)/$', views.track_details, name='details'),
]

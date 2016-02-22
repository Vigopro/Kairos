from django.conf.urls import url
from . import views
 

urlpatterns = [
    url(r'^(?:(?P<id>\d+)/)?$', views.index, name = "index"),
    url(r'^good/(?P<id>\d+)/$', views.good, name = "good"),
]
 
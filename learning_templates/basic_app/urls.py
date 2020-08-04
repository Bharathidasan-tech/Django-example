from django.conf.urls import url
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    url(r'^relative/$', views.urltemplate, name='urltemplate'),
    url(r'^other/$', views.other, name='other'),
]
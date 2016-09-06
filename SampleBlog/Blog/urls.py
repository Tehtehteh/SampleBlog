from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.homepage),
    url(r'^api/blogposts', views.getBlogPosts),
]
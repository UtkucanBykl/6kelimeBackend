from django.urls import re_path

from .views import PostCreateApiView, UserPostListView

app_name = 'core'

urlpatterns = [

    # /post/create/
    re_path(r'^create-post/$', PostCreateApiView.as_view(), name='post-create'),

    # /my-post
    re_path(r'^my-post/$', UserPostListView.as_view(), name='post-user'),

]
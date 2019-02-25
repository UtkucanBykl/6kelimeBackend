from django.urls import re_path
from .views import PostCreateApiView, UserPostListView, PostDetailApiView, CategoryPostsListView, LoginView

app_name = 'core'

urlpatterns = [

    # /post/create/
    re_path(r'^create-post/$', PostCreateApiView.as_view(), name='post-create'),

    # /my-posts
    re_path(r'^my-posts/$', UserPostListView.as_view(), name='post-user'),

    # /detail/{slug}/
    re_path(r'^post/(?P<slug>[\w-]+)/$',  PostDetailApiView.as_view(), name='post-detail'),

    # /login
    re_path(r'^login/', LoginView.as_view(), name='login'),
  
    # /posts/category/{cat_name}
    re_path(r'^post/category/(?P<cat_name>[\w-]+)/$', CategoryPostsListView.as_view(), name='post-category'),

]
from django.urls import re_path

from .views import (
    PostCreateApiView,
    UserPostListView,
    PostDetailApiView,
    CategoryPostsListView,
    LoginView,
    RegisterView,
    LikeCreateOrDeleteView,
    MostLikeListView
)


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

    # /register
    re_path(r'^register/', RegisterView.as_view(), name='register'),

    # /like/post/{slug}
    re_path(r'^like/post/(?P<slug>[\w-]+)/$', LikeCreateOrDeleteView.as_view(), name='like-create'),

    # /like/post/{slug}
    re_path(r'^most/like/post/$', MostLikeListView.as_view(), name='most-like'),

]
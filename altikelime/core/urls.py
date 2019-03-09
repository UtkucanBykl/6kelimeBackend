from django.urls import re_path

from .views import (
    PostCreateApiView,
    UserPostListView,
    PostDetailApiView,
    CategoryPostsListView,
    LoginView,
    RegisterView,
    LikeCreateOrDeleteView,
    MostLikeListView,
    PostDeleteApiView,
    PostUnpublishListAPIView,
    CommentCreateApiView,
    LikeListAPIView,
    PostCommentListApiView,
    PostSearchListAPIView,
    FollowCreateAPIView,
    CommentDeleteApiView,

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

    # /most/like/post
    re_path(r'^most/like/post/$', MostLikeListView.as_view(), name='most-like'),

    # /delete/post/{slug}
    re_path(r'^delete/post/(?P<slug>[\w-]+)/$', PostDeleteApiView.as_view(), name='post-delete'),

    # /unpublish/post/
    re_path(r'^unpublish/$', PostUnpublishListAPIView.as_view(), name='post-list-unpublish'),

    # /comment/create/{slug}
    re_path(r'^create-comment/(?P<slug>[\w-]+)/$', CommentCreateApiView.as_view(), name='comment-create'),

    # /{slug}/likes/
    re_path(r'^(?P<slug>[\w-]+)/likes/$', LikeListAPIView.as_view(), name='like-list'),

    # /comment/list/{slug}
    re_path(r'^create-list/(?P<slug>[\w-]+)/$', PostCommentListApiView.as_view(), name='comment-list'),

    # /comment/delete/{slug}
    re_path(r'^create-delete/(?P<slug>[\w-]+)/$', CommentDeleteApiView.as_view(), name='comment-delete'),

    # /follow/{username}/
    # /search/post/?content={content}&username={username}/
    re_path(r'^search/post/$', PostSearchListAPIView.as_view(), name='post-search'),

    # /follow/{username}/
    re_path(r'^follow/$', FollowCreateAPIView.as_view(), name='follow-create')

]
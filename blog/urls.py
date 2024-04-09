from django.contrib import admin
from django.urls import path
from blog.views import PostView, ListPostView, LikePostView, LikesCountView

urlpatterns = [
    
    path('post/', PostView.as_view()),
    path('list-post/', ListPostView.as_view()),
    path('like/', LikePostView.as_view(), name='like-post'),
    path('likes/', LikesCountView.as_view(), name='likes-count')
]
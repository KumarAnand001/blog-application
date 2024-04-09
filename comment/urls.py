from django.contrib import admin
from django.urls import path
from comment.views import CommentView

urlpatterns = [
    
    path('cmts/', CommentView.as_view()),
]
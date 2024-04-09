from rest_framework import serializers
from .models import Post, Like

class PostSerializer(serializers.ModelSerializer):

    class Meta:

        model = Post
        exclude = ['published_date',]

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'



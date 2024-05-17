from rest_framework import serializers
from .models import Category, Post, Comment, Like, Trend

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'author', 'summary']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['status']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['name', 'author', 'summary', 'img', 'video', 'audio']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['name', 'author']

class TrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trend
        fields = ['name', 'author', 'summary', 'img', 'video', 'audio']

from rest_framework import viewsets
from .models import Category, Post, Comment, Like, Trend
from .serializers import CategorySerializer, PostSerializer, CommentSerializer, LikeSerializer, TrendSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class TrendViewSet(viewsets.ModelViewSet):
    queryset = Trend.objects.all()
    serializer_class = TrendSerializer

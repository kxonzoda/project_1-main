from django.contrib import admin
from blog.models import Category, Post, Comment, Like, Trend


admin.site.register([Category, Post, Comment, Like, Trend])

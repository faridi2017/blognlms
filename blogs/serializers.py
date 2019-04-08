from rest_framework import serializers
from .models import *
import json
from rest_framework.response import Response
from rest_framework.serializers import SerializerMethodField
from rest_framework.parsers import MultiPartParser, FormParser


class BlogImageSerializer(serializers.ModelSerializer):
  class Meta():
    model = BlogImage
    fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class BlogwithcommentSerializer(serializers.ModelSerializer):
    blog_comments = CommentSerializer(read_only=True, many=True)
    blog_image = BlogImageSerializer(read_only=True)
    class Meta:
        model = Blog
        fields = ('id','title','content','created_on','datemodified','author','numberofcomment','blog_comments', 'blog_image')


class BloguserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bloguser
        fields = '__all__'
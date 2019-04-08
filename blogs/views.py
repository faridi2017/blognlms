# djangotemplates/example/views.py
from django.shortcuts import render
from rest_framework.response import Response
from django.views.generic import TemplateView # Import TemplateView
from rest_framework import status
from rest_framework.views import APIView
from .serializers import *
from rest_framework import generics
import json

# Create your views here.
class BlogView(APIView):
    def post(self, request, *args, **kwargs):
        file_serializer = BlogSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        blogid = request.GET.get('blogid')
        if blogid:
            record = Blog.objects.get(pk=blogid)
            serializer = BlogSerializer(record)
            return Response(serializer.data)
        documents = Blog.objects.all()
        serializer = BlogSerializer(documents,many=True)
        return Response(serializer.data)

    def put(self, request):
        blogid = request.GET.get('blogid')
        record = Blog.objects.get(pk=blogid)
        serializer = BlogSerializer(record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentView(APIView):
    def post(self, request, *args, **kwargs):
        file_serializer = CommentSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        blogid = request.GET.get('blogid')
        if blogid:
            record = Comment.objects.filter(blogid=blogid)
            serializer = CommentSerializer(record,many=True)
            return Response(serializer.data)
        documents = Comment.objects.all()
        serializer = CommentSerializer(documents,many=True)
        return Response(serializer.data)

class BloguserList(APIView):
    def get(self,request):
        documents = Bloguser.objects.all()
        serializer = BloguserSerializer(documents,many=True)
        return Response(serializer.data)

    def post(self, request, Format=None):
        print('received data',request.data)
        serializer = BloguserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Blogncomment(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogwithcommentSerializer

class Comments(APIView): #get one, delete one
    def get(self,request,id):
        document = Comment.objects.get(id=id)
        serializer = CommentSerializer(document)
        return Response(serializer.data)

    def delete(self, request,id):
        record = Comment.objects.get(id=id)
        if record:
            record.delete()
            return Response({"message": "Comments with id `{}` has been deleted.".format(id)}, status=204)
        return Response('this id does not  exist',status=status.HTTP_400_BAD_REQUEST)
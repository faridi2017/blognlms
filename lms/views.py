# djangotemplates/example/views.py
from django.shortcuts import render
from django.views.generic import TemplateView # Import TemplateView
from rest_framework import status
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
import pandas as pd
import json
import xlrd
class BooksList(APIView): #get one, delete one
    def get(self,request):
        document = Books.objects.all()
        serializer = BooksSerializer(document,many=True)
        return Response(serializer.data)
    def post(self, request, Format=None):
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentList(APIView): #get one, delete one
    def get(self,request):
        document = Students.objects.all()
        serializer = StudentsSerializer(document,many=True)
        return Response(serializer.data)

class Upload_excel_file_books(APIView):
    def post(self, request):
        f = request.FILES['file']
        myfile = pd.read_excel(f)
        booklist = myfile.to_json(orient='records')
        booklist = json.loads(booklist)
        # print(booklist)
        serializer = BooksSerializer(data=booklist, many=True)
        if serializer.is_valid():
            serializer.save()
        return Response('success')

class Upload_excel_file_students(APIView):
    def get(self,request):
        document = Students.objects.all()
        serializer = StudentsSerializer(document,many=True)
        return Response(serializer.data)

    def post(self, request):
        f = request.FILES['file']
        myfile = pd.read_excel(f)
        student_list = myfile.to_json(orient='records')
        student_list = json.loads(student_list)
        serializer = StudentsSerializer(data=student_list, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CheckoutsList(APIView):
    def get(self,request):
        document = Checkouts.objects.all()
        serializer = CheckoutsSerializer(document,many=True)
        return Response(serializer.data)

    def post(self, request):
        book_list = request.data
        serializer = CheckoutsSerializer(data=book_list, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CheckoutsWithStudent(APIView):
    def get(self,request):
        document = Students.objects.all()
        serializer = StudentWithBooks(document,many=True)
        return Response(serializer.data)


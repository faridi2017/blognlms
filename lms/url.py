# djangotemplates/crm/urls.py
from django.conf.urls import url
from . import views
from django.urls import path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from lms import views

urlpatterns = [
    path('books/', views.BooksList.as_view()),
    path('students/', views.StudentList.as_view()),
    path('ExcelUploadBooks/', views.Upload_excel_file_books.as_view()),
    path('ExcelUploadStudents/', views.Upload_excel_file_students.as_view()),
    path('checkouts/', views.CheckoutsList.as_view()),
    path('studentscheckouts/', views.CheckoutsWithStudent.as_view()),
]
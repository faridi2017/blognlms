# djangotemplates/crm/urls.py
from django.conf.urls import url
from . import views
from django.urls import path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from blogs import views

urlpatterns = [
    path('bloguser/', views.BloguserList.as_view()), #http://192.168.0.21:8000/cit/bloguser/
    path('blog/', views.BlogView.as_view()), #faridi/aarif/
    path('comment/', views.CommentView.as_view()), #faridi/aarif/
    path('blogscmt/', views.Blogncomment.as_view()), #http://192.168.0.21:8000/cit/blogscmt/

]

'''
Server	manny.db.elephantsql.com (manny-01)
User & Default database:	hkxgbizo
Password	uFPwTYiPIsNjBsAQW6onmU3Nh46806J5
URL:	postgres://hkxgbizo:uFPwTYiPIsNjBsAQW6onmU3Nh46806J5@manny.db.elephantsql.com:5432/hkxgbizo
Max database size	20 MB
API Key 65a9b614-91ed-4967-8cf2-7f81c23807fc
API documentation is here: https://docs.elephantsql.com/elephantsql_api.html
hamdard/#hamdard@123

'''
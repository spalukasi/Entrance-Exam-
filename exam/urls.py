
from django.conf.urls import url, patterns,include 
from django.contrib import admin
from entrance.views import student_detail, index, Login, HomePage, login, loginform, search, signupform,test

#from .entrance import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',HomePage),
    url(r'^loginform/$',loginform),
    url(r'^signupform/$',signupform),
    url(r'^test/$',test),





    url(r'^form/$',Login),
    url(r'^search/$',search),
    url(r'^Login/$',login),
    #url(r'^hello/$',hello),
    url(r'^student/$',index),
    url(r'^student/(?P<student_id>[0-9]+)/$',student_detail),
    
]
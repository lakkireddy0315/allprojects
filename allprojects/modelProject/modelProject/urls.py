"""modelProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from testApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('display_dtl/',views.display_view),
    path('employee_data_view/', views.employee_data_view),
    path('employee_data_jsonview/', views.employee_data_jsonview),
    url(r'^movies/', views.moviesInfo),
    url(r'^sports/', views.sportsInfo),
    url(r'^politics/', views.politicsInfo),
    #url(r'^$', views.index),
    path('students/', views.studentview),
    path('pdf/', views.getpdf),
    path('formstest/', views.studentinputview),
    path('input/', views.student_input_view),
    path('signup/', views.signup_view),
    path('fEEDBACK/', views.feedback_form_view),
    #path('modelform/', views.student_view),
    path('indexview/', views.index_view),
    path('addmovie/', views.add_movie_view),
    path('listmovies/', views.list_movie_view),
    path('countcookie/', views.count_view),
    path('name/', views.name_view),
    path('gf/', views.gf_view),
    path('results/', views.results_view),
    path('age/', views.age_view),
    path('index/', views.index),
    path('index1/', views.index1),
    path('add/', views.additem),
    path('display/', views.displayitem_view),
    path('accounts/',include('django.contrib.auth.urls')),
    url(r'^$', views.home_page_view),
    path('python/', views.python_exams_view),
    path('java/', views.java_exams_view),
    path('aptitude/', views.aptitude_exams_view),
    path('logout/', views.logout_view),
    #path('signup/', views.signup_view),
    path('classtest/', views.HelloWorldView.as_view()),
    path('modelclasstest/', views.BookListView.as_view()),
    #path('BeerListView/', views.BeerListView.as_view()),
    #url(r'^$', views.BeerListView.as_view(),name='home'),
    url(r'^show_view', views.show_view,name='home'),
    url(r'^$', views.post_list_view),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', views.post_detail_view,name='post_detail'),
    url(r'^insert/', views.insert_view),
    url(r'^delete/(?P<id>\d+)/$', views.delete_view),
    url(r'^update/(?P<id>\d+)/$', views.update_view),
    url(r'^(?P<pk>\d+)/$', views.BeerDetailView.as_view(),name='detail'),
    url(r'^create/', views.BeerCreateView.as_view()),
    #url(r'^update/(?P<pk>\d+)/$', views.BeerUpdateView.as_view()),
    #url(r'^delete/(?P<pk>\d+)/$', views.BeerDeleteView.as_view()),
    path('emp_view/', views.display_view),
    path('welcome_view/', views.welcome_view),
    path('home_page_view1/', views.home_page_view1),
    url(r'^(?P<id>\d+)/share/$', views.mail_send_view),
]

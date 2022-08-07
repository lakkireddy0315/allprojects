"""serializers URL Configuration

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
from django.urls import path
from django.conf.urls import include, url
from testApp import views
from rest_framework import routers
#from testApp.views import EmployeeCRUDCBV
from rest_framework.authtoken import views as views1
from rest_framework.authtoken.views import obtain_auth_token
router=routers.DefaultRouter()
#outer.register('test-viewset',views.TestViewSet,'test-viewset')
router.register('api1',views.EmployeeCRUDCBV)
#router.register(r'api',EmployeeCRUDCBV,'EmployeeCRUDCBV')
#from rest_framework.authtoken import views

urlpatterns = [
    path('signup/', views.signup_view),
    path('admin/', admin.site.urls),
    path('hello/', views.HelloView.as_view(), name='hello'),
    #path('employee_data_view/',views.employee_data_view),
    path('employee_data_jsonview/',views.employee_data_jsonview),
    #path('EmployeeCRUDCBV/<id>/',views.EmployeeCRUDCBV.as_view()),
    #path('EmployeeListCBV/<id>',views.EmployeeListCBV.as_view()),
    url(r'^cbv1/', views.JsonCBV.as_view()),
    #url(r'^api/(?P<id>\d+)/$', views.EmployeeCRUDCBV.as_view()),
    #url(r'^EmployeeCRUDCBV/(?P<id>\d+)/$', views.EmployeeCRUDCBV.as_view()),
    #url(r'^api/(?P<id>\d+)/$', views.EmployeeRetrieveUpdateDestroyAPIView.as_view()),
    url(r'',include(router.urls)),
    #url(r'^get-api-token/', views.obtain_auth_token,name='get-api-token'),
    path('index/',views.index),
    path('hydjobs/',views.hydjobs1),
    path('EmployeeAPIView/',views.EmployeeAPIView.as_view()),
    #url(r'^api/', views.TestViewSet.as_view()),
    #url(r'^api/', views.StudentCRUDCBV.as_view()),
    #url(r'^api/', views.TestApiView.as_view()),
    #url(r'^api/', views.EmployeeListAPIView.as_view()),
    #url(r'', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    url(r'^get-api-token/', views1.obtain_auth_token,name='get-api-token'),
    #url(r'^api/$', views.EmployeeListModelMixin.as_view()),
    #url(r'^api/(?P<pk>\d+)/$', views.EmployeeDetailAPIViewMixin .as_view()),
    url(r'^author-api/$', views.AuthorListView.as_view()),
    url(r'^author-api/(?P<pk>\d+)/$', views.AuthorView.as_view()),
    url(r'^book-api/$', views.BookListView.as_view()),
    url(r'^book-api/(?P<pk>\d+)/$', views.BookView.as_view()),
    url(r'^info/', views.get_geographic_info),
]

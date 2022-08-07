from django.conf.urls import url
from django.urls import path
from testapp import views
urlpatterns = [
path('first/', views.first_view),
]

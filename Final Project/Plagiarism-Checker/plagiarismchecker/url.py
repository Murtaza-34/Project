from django.urls import path
from . import views
from .views import register,login
urlpatterns = [
    path('', views.home,name='plagiarism-check-mainpage'),
    path('compare/', views.fileCompare,name='compare'), 
    path('test/', views.test,name='Test'),
    path('filetest/', views.filetest,name='filetest'),
    path('twofiletest1/', views.twofiletest1,name='twofiletest1'),
    path('twofilecompare1/', views.twofilecompare1,name='twofilecompare1'),
    path('register/', views.register, name='register'),
    path('login/',views.login, name='login'),
    path('logout/',views.logoutUser,name='logout')
      
]
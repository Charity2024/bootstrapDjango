from django.urls import path
from Myapp import views

urlpatterns = [
    path('', views.home, name='my_home'),
    path('page/', views.innerpage, name='innerpage')

]

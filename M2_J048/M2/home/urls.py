from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('more/<str:pk>/', views.more, name='more'),
    path('add/', views.add, name='add'),
    path('delete/<str:id>/', views.delete, name='delete'),
    path('update/<str:id>/', views.update, name='update'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contactus/', views.contactus, name='contactus'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('signup/', views.signup, name='signup')
]
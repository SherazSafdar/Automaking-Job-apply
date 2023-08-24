from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('home/', views.homepage, name='home'),
    path('verify/<uuid:token>/', views.verify_email, name='verify_email'),
    
    
]



from django.urls import path
from . import views 


urlpatterns = [
    path('register/', views.RegisterView, name= 'user_register'),
    path('login/', views.LoginView, name= 'user_login'),
    path('logout/', views.LogoutView, name= 'user_logout'),
]

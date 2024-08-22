from django.urls import path
from user.views import user_register, user_login

urlpatterns = [
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'), 
]


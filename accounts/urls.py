from django.urls import path
from .views import user_login , user_logout  , register



urlpatterns = [
    path('login/',user_login,name='user-login'),
    path('logout/',user_logout,name='user-logout'),
    path('register/',register,name='user-register'),
]
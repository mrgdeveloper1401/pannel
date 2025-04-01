from rest_framework.urls import path

from . import views

app_name = 'api_v1_auth'

urlpatterns = [
    path('login/', views.UserLoginApiView.as_view(), name='login'),
    path('profile/', views.UserProfileApiView.as_view(), name='profile'),
]

from .views import CandidateView, RegisterAPI, UpdateProfile
from django.urls import path
from knox import views as knox_views
from .views import LoginAPI

urlpatterns = [
    path('', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/<int:pk>/update-profile/', UpdateProfile.as_view(), name='update-profile'),
]

from django.urls import path
from main_app import views

urlpatterns = [
    path('auth/', views.SignInView.as_view(), name='gen_auth'),
]

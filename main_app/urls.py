from django.urls import path
from main_app import views

urlpatterns = [
    path('auth/', views.SignInView.as_view(), name='gen_auth'),
    path('file-manager/', views.FileManagementView.as_view(), name='file-manager'),
    path('file-reader/', views.FileReaderView.as_view(), name='file-reader'),
]

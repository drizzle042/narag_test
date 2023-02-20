from django.urls import path
from django.views.generic import TemplateView
from main_app import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='main.html'), name='main-user-interface'),
    path('auth/', views.SignInView.as_view(), name='gen_auth'),
    path('file-manager/', views.FileManagementView.as_view(), name='file-manager'),
    path('file-reader/', views.FileReaderView.as_view(), name='file-reader'),
]

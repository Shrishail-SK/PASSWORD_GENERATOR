from django.urls import path
from . import views

urlpatterns = [
    path('', views.password_generator_view, name='password_generator'),
    path('save/<str:service_name>/<str:password>/', views.save_service_password, name='save_service_password'),
    path('retrieve/<str:service_name>/', views.retrieve_password_view, name='retrieve_password'),
    path('main/', views.main_page_view, name='main_page'),
]

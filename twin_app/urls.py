# twin_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Path for the new main landing page (e.g., http://127.0.0.1:8000/)
     path('', views.landing_page, name='landing_page'),
    path('app/', views.index_page, name='app_home'),
    
    # Path for the registration form
    path('register/', views.register_user, name='register_user'),
    
    # Path for the dashboard that lists all users
    path('dashboard/', views.dashboard_list, name='dashboard_list'),
    path('update/<int:profile_id>/', views.update_user, name='update_user'),
    
    # Path for the detailed analysis of a single user
    path('dashboard/<int:profile_id>/', views.profile_dashboard, name='profile_dashboard'),
     path('demo/', views.roshan_demo_view, name='roshan_demo'),
     path('send-email/<str:email>/', views.send_email, name='send_email'),

   path('delete-user/<int:user_id>/', views.delete_user, name='delete_user'),
]
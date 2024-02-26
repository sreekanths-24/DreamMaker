from django.urls import path
from . import views
urlpatterns = [
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('register_user/', views.register_user, name='register_user'),
    path('profile/<int:id>/', views.profile, name='profile'),
    path('profile/<int:id>/add_more_details_to_profile', views.add_more_details_to_profile, name='add_more_details_to_profile'),
    path('profile/<int:id>/edit_account_info', views.edit_account_info, name='edit_account_info'),
]

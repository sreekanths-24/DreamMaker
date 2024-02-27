"""my_todo_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # Add this line to include the include function
from django.conf import settings
from django.conf.urls.static import static
from eventmanagement import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')), # Add this line to include the core app's URLs
    path('users/', include('django.contrib.auth.urls')), # Add this line to include the users app's URLs
    path('users/', include('users.urls')),
    path('eventmanagement/', include('eventmanagement.urls')), # Add this line to include the eventmanagement app's URLs
    path('all_events/', views.all_events, name='all_events'),
    path('add_event/', views.add_event, name='add_event'),
    path('update_event/', views.update_event, name='update_event'),
    path('remove/', views.remove, name='remove'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)# Add this line to include the core app's URLs

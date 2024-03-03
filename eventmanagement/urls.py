from django.urls import path
from . import views
urlpatterns = [
    path('events', views.events, name='events'),
    path('event_detail/<int:id>', views.event_detail, name='event_detail'),
    path('event_delete/<int:id>', views.event_delete, name='event_delete'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('todos/', views.todos, name='todos'),  # Add a trailing slash for consistency
    path('todo_detail/<int:id>/', views.todo_detail, name='todo_detail'),  # Add a trailing slash for consistency
    path('todo_detail/<int:id>/mark_completed/', views.mark_completed, name='mark_completed'),  # Add a trailing slash for consistency
    path('todo_detail/<int:id>/mark_uncompleted/', views.mark_uncompleted, name='mark_uncompleted'),  # New URL mapping for mark_uncompleted
    path('todo_detail/<int:id>/todo_delete/', views.todo_delete, name='todo_delete'),  # New URL mapping for 
    path('todo_detail/<int:id>/todo_edit/', views.todo_edit, name='todo_edit'),  # New URL mapping for
    path('AddDreamFormView', views.AddDreamFormView, name='AddDreamFormView'),  # New URL mapping for AddDreamFormView
    path('DreamAchievedFormView', views.DreamAchievedFormView, name='DreamAchievedFormView'),  # New URL mapping for DreamAchievedFormView
    path('discard_dream/', views.discard_dream, name='discard_dream'),
    path('download_report/', views.download_report, name='download_report'),
]

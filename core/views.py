from datetime import datetime, date
from django.shortcuts import render, redirect
from .models import Todo
from eventmanagement.models import Events
from django.contrib import messages
from .forms import *
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        username = request.user.username
        profile_image = request.user.profile.image.url
        name = request.user.first_name + ' ' + request.user.last_name
        return render(request, 'index.html' , {'username': username, 'profile_image': profile_image, 'name': name})
    else:
        return render(request, 'index.html')

def todos(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            title = request.POST['title']
            description = request.POST['description']
            duedate_str = request.POST['duedate']
            complete = False

            # Parse the due date string to a date object
            duedate = datetime.strptime(duedate_str, '%Y-%m-%d').date()

            # Check if the due date is in the past
            if duedate < date.today():
                messages.error(request, "Due date cannot be in the past.")
                return redirect('todos')
            # Create a new todo object and save it to the database
            ob = Todo(title=title, description=description, complete=complete, user=request.user, duedate=duedate)
            ob.save()
            # Add the todo to the calendar
            # obj = Events(user = request.user, name = title, startdate = duedate, enddate = duedate, description = description)
            # obj.save()

            
            messages.success(request, 'Todo added successfully and marked in calendar.')

            return redirect('todos') 
        else:
            obj = Todo.objects.filter(user=request.user).all()
            username = request.user.username
            name = request.user.first_name + ' ' + request.user.last_name
            profile_image = request.user.profile.image.url
            return render(request, 'todos.html', {'todos': obj, 'username': username, 'profile_image': profile_image, 'name': name})
    else:
        messages.success(request, "You must be logged in to view todos.")
        return redirect('index')

def todo_detail(request, id):
    if request.user.is_authenticated:
        obj = Todo.objects.get(id=id)
        username = request.user.username
        profile_image = request.user.profile.image.url
        name = request.user.first_name + ' ' + request.user.last_name
        return render(request, 'todos_details.html', {'todo': obj, 'username': username, 'profile_image': profile_image, 'name': name})
    else:
        messages.success(request, "You must be logged in to view todos.")
        return redirect('index')

def mark_completed(request, id):
    if request.user.is_authenticated:
        obj = Todo.objects.get(id=id)
        obj.complete = True
        obj.save()
        messages.success(request, 'Todo marked as completed')
        return redirect('todos')
    else:
        messages.success(request, "You must be logged in to mark todos as completed.")
        return redirect('index')

def mark_uncompleted(request, id):  # New view function to mark a task as uncompleted
    if request.user.is_authenticated:
        obj = Todo.objects.get(id=id)
        obj.complete = False
        obj.completed_at = None  # Set completed_at to None when marking as uncompleted
        obj.save()
        messages.success(request, 'Todo marked as uncompleted')
        return redirect('todos')
    else:
        messages.success(request, "You must be logged in to mark todos as uncompleted.")
        return redirect('index')

def todo_delete(request, id):  # New view function to delete a task
    if request.user.is_authenticated:
        obj = Todo.objects.get(id=id)
        obj.delete()
        messages.success(request, 'Todo deleted successfully')
        return redirect('todos')
    else:
        messages.success(request, "You must be logged in to delete todos.")
        return redirect('index')

def todo_edit(request, id):  # New view function to edit a task
    if request.user.is_authenticated:    
        current_todo = Todo.objects.get(id=id)
        save_current_todo = current_todo
        form = TodoEditForm(request.POST or None, instance=current_todo)
        if form.is_valid():
            form.save()
            messages.success(request, "Todo  updated successfully!!")
            return redirect('todos')

        # Check if the title of the todo has been updated
        # current_todo = Todo.objects.get(id=id)
        # print(save_current_todo.title)
        # print(current_todo.title)
        # if save_current_todo != current_todo:
        #     obj = Events.obejects.get(name=save_current_todo.title, user=request.user)
        #     obj.name = current_todo.title
        #     messages.success(request, "Title updated in the calendar successfully!!")
        #     return redirect('todos')
        username = request.user.username
        profile_image = request.user.profile.image.url
        name = request.user.first_name + ' ' + request.user.last_name
        return render(request, 'todo_edit.html', {'form':form, 'username': username, 'profile_image': profile_image, 'name': name})
    else:
        messages.success(request, "You must be logged in to edit todos.")
        return redirect('index')
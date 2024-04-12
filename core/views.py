from datetime import datetime, date
from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo, Dream
from eventmanagement.models import Events
from django.contrib import messages
from .forms import *
from django.utils import timezone
from datetime import date, timedelta
from .forms import AddDreamForm, DreamAchievedForm
from django.db.models import F
from .utils import generate_goal_journey_report_image
from django.http import HttpResponse

def handler404(request):
    return render(request, '404.html')
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        username = request.user.username
        profile_image = request.user.profile.image.url
        name = request.user.first_name + ' ' + request.user.last_name
        return render(request, 'index.html' , {'username': username, 'profile_image': profile_image, 'name': name})
    else:
        return render(request, 'index.html')

def dashboard(request):
    if request.user.is_authenticated:
        username = request.user.username
        profile_image = request.user.profile.image.url
        name = request.user.get_full_name()
        todaysdate = timezone.now().date()

        # Filter events whose end date is 1 week or less from now
        one_week_from_now = timezone.now() + timedelta(days=7)
        events = Events.objects.filter(user=request.user, enddate__lte=one_week_from_now)

        if request.user.dream:
            # Initialize dream-related forms and variables
            form_1 = AddDreamForm(request.POST or None, instance=request.user.dream, initial={'user': request.user})
            form_2 = DreamAchievedForm(request.POST or None, instance=request.user.dream, initial={'user': request.user})
            current_dream_of_user = None
        else:
            request.user.dream = "Empty Dream"
            form_1 = AddDreamForm(request.POST or None, instance=request.user.dream, initial={'user': request.user})
            form_2 = DreamAchievedForm(request.POST or None, instance=request.user.dream, initial={'user': request.user})
            current_dream_of_user = None

        try:
            current_dream_of_user = request.user.dream
        except Dream.DoesNotExist:
            current_dream_of_user = "Empty Dream"

        context = {
            'username': username, 
            'profile_image': profile_image, 
            'name': name,
            'events': events,
            'todaysdate': todaysdate,
            'form_1': form_1,
            'form_2': form_2,
            'current_dream_of_user': current_dream_of_user   
        }

        return render(request, 'dashboard.html', context)
    else:
        return redirect('index')

def discard_dream(request):
    if request.method == 'POST':
        # Check if a Dream object exists for the current user
        if Dream.objects.filter(user=request.user).exists():
            current_dream_of_user = get_object_or_404(Dream, user=request.user)
            todos = Todo.objects.filter(dream=current_dream_of_user)
            events = Events.objects.filter(dream=current_dream_of_user)

            # Delete all todos associated with the dream
            todos.delete()

            # Delete all events associated with the dream
            events.delete()

            # Rename the dream to something else (for example, 'Discarded Dream')
            current_dream_of_user.title = 'Now set a new goal/dream e.g. "Learn Python" or "Get a new job"'
            current_dream_of_user.save()

            messages.success(request, "Dream discarded successfully!")
        else:
            messages.error(request, "You don't have a dream to discard.")

        return redirect('dashboard')

    return render(request, 'dashboard.html')


def AddDreamFormView(request):
    if request.user.is_authenticated:
        form = AddDreamForm(request.POST or None, instance=request.user.dream, initial={'user': request.user})
        if form.is_valid():
            form.save()
            messages.success(request, "Dream updated successfully!!")
            return redirect('dashboard')
        else:
            messages.error(request, "An error occurred while updating your dream. Please try again.")
            return redirect('dashboard')
    else:
        messages.success(request, "You must be logged in to add a dream.")
        return redirect('index')

def DreamAchievedFormView(request):
    if request.user.is_authenticated:
        form = DreamAchievedForm(request.POST or None, instance=request.user.dream, initial={'user': request.user})
        if form.is_valid():
            form.save()
            if request.user.dream.achieved:
                messages.success(request, "congratulations for achieving your dream!!")
            else:
                messages.success(request, "Dream updated successfully!!")
            return redirect('dashboard')
        else:
            messages.error(request, "An error occurred while updating your dream. Please try again.")
            return redirect('dashboard')
    else:
        messages.success(request, "You must be logged in to mark a dream as achieved.")
        return redirect('index')


def todos(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            title = request.POST['title']
            description = request.POST['description']
            duedate_str = request.POST['duedate']
            complete = False
            priority = request.POST['priority']
            # Parse the due date string to a date object
            duedate = datetime.strptime(duedate_str, '%Y-%m-%d').date()

            # Check if the due date is in the past
            if duedate < date.today():
                messages.error(request, "Due date cannot be in the past.")
                return redirect('todos')
            # Create a new todo object and save it to the database
            ob = Todo(title=title, description=description, complete=complete, user=request.user, duedate=duedate, priority=priority, dream=request.user.dream)
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


def download_report(request):
    if request.user.is_authenticated:
        # Fetch data from the database
        user = request.user
        try:
            current_dream = user.dream
            todos = Todo.objects.filter(user=user, dream=current_dream)
            events = Events.objects.filter(user=user, dream=current_dream)
        except Dream.DoesNotExist:
            current_dream = None
            todos = None
            events = None

        # Generate goal journey report image
        report_image_data = generate_goal_journey_report_image(user, current_dream, todos, events)

        # Return the image as a downloadable file
        response = HttpResponse(content_type='image/png')
        response['Content-Disposition'] = 'attachment; filename="goal_journey_report.png"'
        response.write(report_image_data)
        return response
    else:
        return HttpResponse("You must be logged in to download the report.")

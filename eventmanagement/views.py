from django.shortcuts import render
from django.http import JsonResponse
from core.models import Todo
from .models import *
# Create your views here.
def events(request):
    if request.user.is_authenticated:
        all_events = Events.objects.filter(user=request.user)
        
        username = request.user.username
        profile_image = request.user.profile.image.url
        name = request.user.first_name + ' ' + request.user.last_name
        
        context = {
            'events': all_events,
            'username': username, 
            'profile_image': profile_image, 
            'name': name
        }

        return render(request, 'events.html', context)
    else:
        messages.success(request, "You must be logged in to view your events.")
        return redirect('index')

def all_events(request):
    all_events = Events.objects.filter(user=request.user)
    all_todos = Todo.objects.filter(user=request.user)
    out = []
    for event in all_events:
        out.append({
            'title': event.name,
            'id': event.id,
            'start': event.startdate.strftime("%m/%d/%Y, %H:%M:%S"),                                                         
            'end': event.enddate.strftime("%m/%d/%Y, %H:%M:%S"),
        })
    for event in all_todos:
        out.append({
            'title': event.title,
            'id': event.id,
            'start': event.duedate.strftime("%m/%d/%Y, %H:%M:%S"),                                                         
            'end': event.duedate.strftime("%m/%d/%Y, %H:%M:%S"),
        })
    return JsonResponse(out, safe=False)

def add_event(request):
    startdate = request.GET.get('start', None)
    enddate = request.GET.get('end', None)
    title = request.GET.get('title', None)
    description = request.GET.get('description', None)
    event = Events(name=title, startdate=startdate, enddate=enddate, description=description, user=request.user)
    event.save()
    data = {}
    return JsonResponse(data)

def update_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    description = request.GET.get("description", None)
    print("start = " + start +"end = "+ end +"title = "+ title +"id = "+ id +"description = "+ str(description))
    event = Events.objects.get(id=id, user=request.user)
    event.startdate = start
    event.enddate = end
    event.name = title
    event.save()

    # todo = Todo.objects.get(name=title, user=request.user)
    # todo.duedate = start
    # todo.save()

    data = {}
    return JsonResponse(data)

def remove(request):
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id, user=request.user)
    event.delete()
    data = {}
    return JsonResponse(data)
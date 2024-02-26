from django.shortcuts import render

# Create your views here.
def events(request):
    if request.user.is_authenticated:
        username = request.user.username
        profile_image = request.user.profile.image.url
        name = request.user.first_name + ' ' + request.user.last_name
        return render(request, 'events.html', { 'username': username, 'profile_image': profile_image, 'name': name})
    else:
        messages.success(request, "You must be logged in to view your events.")
        return redirect('index')

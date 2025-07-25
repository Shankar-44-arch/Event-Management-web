from django.shortcuts import render, redirect
from .models import Event
from .forms import EventForm
# Create your views here.
def home(request):
    events = Event.objects.all()
    return render(request, 'home.html' ,{'events': events})

def detail(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EventForm()
    return render(request, 'details.html', {'form': form})


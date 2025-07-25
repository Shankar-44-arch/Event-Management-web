from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['eventName', 'collegeName', 'startDate', 'endDate','events' , 'contact', 'location', 'link']
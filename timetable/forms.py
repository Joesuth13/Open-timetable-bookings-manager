from django import forms
from .models import Timetable

class MyModelForm(forms.ModelForm):
    # Define the available choices for selection
    available_days = [
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
        ('SUN', 'Sunday'),
    ]
    
    selected_days = forms.MultipleChoiceField(
        choices=available_days,
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    startTime = forms.TimeInput()
    class Meta:
        model = Timetable
        fields = ['name', 'active', 'selected_days','startTime', 'endTime', 'notes']  # Include other fields if necessary
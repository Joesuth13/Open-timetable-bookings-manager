
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.
class UserInfo(AbstractUser):
    
    full_name = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=12)
    ParticipantID = models.ForeignKey('Participant', on_delete=models.CASCADE)


class ClassType(models.Model):
    duration_choices = (('15 Minutes', 15), ('30 Minutes', 30),
                        ('45 Minutes', 45), ('1 Hour', 60),
                        ('1 Hour 15 Minutes', 75), ('1 Hour 30 Minutes', 90),
                        ('1 hour 45 Minutes', 105), ('2 Hours', 120),
                        ('2 Hours 15 Minutes', 135), ('2 Hours 30 Minutes', 150),
                        ('2 Hours 45 Minutes', 165), ('3 Hours', 180),
                        ('3 Hours 15 Minutes', 195), ('3 Hours 30 Minutes', 210),
                        ('3 Hours 45 Minutes', 225), ('4 Hours', 240),
                        ('4 Hours 15 Minutes', 255), ('4 Hours 30 Minutes', 270),
                        ('4 Hours 45 Minutes', 285), ('5 Hours', 300))
    name = models.CharField(max_length=100)
    age_group_min = models.IntegerField()
    age_group_max = models.IntegerField(default=99)
    duration = models.IntegerField(choices = duration_choices)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    defaultCapacity = models.IntegerField()

    class Timetable(models.Model):
        day_choices = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
        name = models.CharField(max_length=200)
        active = models.BooleanField(default=False)
        selected_days = models.JSONField(
        default=list,
        help_text="Store selected days of the week as a JSON array (e.g., ['MON', 'TUE'])"
    )

        startTime = models.TimeField()
        endTime = models.TimeField()
        notes = models.TextField(blank=True)

    class ClassInstance(models.Model):
        class_type = models.ForeignKey('ClassType', on_delete=models.CASCADE)
        instance_date = models.DateTimeField()
        start_time = models.DateTimeField()
        finish_time = models.DateTimeField()
        Capacity = models.IntegerField(0)
        attendees = models.ManyToManyField('Booking')

    class Booking(models.Model):
        userID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        participantID = models.ForeignKey('Participant', on_delete=models.CASCADE)
        instanceID = models.ForeignKey('ClassInstance', on_delete=models.CASCADE)
        paid_or_member = models.BooleanField(default=False)
        created_on = models.DateTimeField(auto_now_add=True)
        updated_on = models.DateTimeField(auto_now=True, blank=True, null=True)
        active = models.BooleanField(default=True)

    class Participant(models.Model):
        name = models.CharField(max_length=200)
        date_of_birth = models.DateField()
        
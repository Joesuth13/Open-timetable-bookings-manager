from django.contrib import admin
from .models import UserInfo, Participant, ClassType, Timetable, ClassInstance, Booking
from .forms import MyModelForm

# Register your models here.
admin.site.register(UserInfo)
admin.site.register(Participant)
admin.site.register(ClassType)

class MyModelAdmin(admin.ModelAdmin):
    form = MyModelForm

    def save_model(self, request, obj, form, change):
        obj.selected_days = form.cleaned_data['selected_days']
        obj.save()

admin.site.register(Timetable, MyModelAdmin)
admin.site.register(ClassInstance)
admin.site.register(Booking)

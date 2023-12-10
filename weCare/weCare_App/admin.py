from django.contrib import admin
from .models import *



admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Feedback)
admin.site.register(Speciality)
admin.site.register(Appointment)
admin.site.register(Location)
admin.site.register(Hospital)



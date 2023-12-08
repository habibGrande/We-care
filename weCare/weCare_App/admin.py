from django.contrib import admin
from .models import *
# import django.apps

# Register your models here.


admin.site.register(Patient)
admin.site.register(Feedback)
admin.site.register(Speciality)
admin.site.register(Appointment)
admin.site.register(Location)
admin.site.register(Hospital)

# models = django.apps.apps.get_models()

# for model in models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass
        

from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Doctor)
admin.site.register(Specialization)
admin.site.register(DoctorSpec)
admin.site.register(Patient)
admin.site.register(Appiontment)
admin.site.register(Report)
admin.site.register(DoctorAvailable)
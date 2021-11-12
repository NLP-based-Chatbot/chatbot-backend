from django.contrib import admin

from transport.models import Vehical_Types
from transport.models import Schedules
from transport.models import Bookings
from transport.models import Offices
from transport.models import Complaints

# Register your models here.
admin.site.register(Vehical_Types)
admin.site.register(Schedules)
admin.site.register(Bookings)
admin.site.register(Offices)
admin.site.register(Complaints)
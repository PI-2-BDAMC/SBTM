from django.contrib import admin

from models import BenchTest
from models import TemperatureSensor

admin.site.register(BenchTest)
admin.site.register(TemperatureSensor)

# Register your models here.

from django.contrib import admin
from .models import Patient,Clinic,Test,TestType,Medic

# Register your models here.

admin.site.register(Patient)

admin.site.register(Clinic)

admin.site.register(Test)

admin.site.register(TestType)

admin.site.register(Medic)
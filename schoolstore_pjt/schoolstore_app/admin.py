from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Department,Course,Order

admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Order)

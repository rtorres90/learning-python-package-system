from django.contrib import admin

# Register your models here.
from models import EmployeeTitle, Store

admin.site.register((Store, EmployeeTitle))
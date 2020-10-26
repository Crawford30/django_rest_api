from django.contrib import admin

#import the models
from hrm.models import *

# Register your models here to be visible in admin section(only the visible class will show).
admin.site.register(Users)


from django.contrib import admin

# Register your models here.

from . models import Admin
from . models import Doctor
from . models import User
from . models import UserSupport
from . models import Assignment
from . models import Report
from . models import Recipe

admin.site.register(Admin)
admin.site.register(Doctor)
admin.site.register(User)
admin.site.register(UserSupport)
admin.site.register(Assignment)
admin.site.register(Report)
admin.site.register(Recipe)
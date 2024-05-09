from django.contrib import admin

# Register your models here.

from api.models.admin_model import Admin
from api.models.doctor_model import Doctor
from api.models.user_model import User
from api.models.user_support_model import UserSupport
from api.models.assignment_model import Assignment
from api.models.report_model import Report
from api.models.recipe_model import Recipe

admin.site.register(Admin)
admin.site.register(Doctor)
admin.site.register(User)
admin.site.register(UserSupport)
admin.site.register(Assignment)
admin.site.register(Report)
admin.site.register(Recipe)
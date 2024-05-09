from django.contrib import admin

# Register your models here.

from api.models.admin.model import Admin
from api.models.doctor.model import Doctor
from api.models.user.model import User
from api.models.user_support.model import UserSupport
from api.models.assignment.model import Assignment
from api.models.report.model import Report
from api.models.recipe.model import Recipe

admin.site.register(Admin)
admin.site.register(Doctor)
admin.site.register(User)
admin.site.register(UserSupport)
admin.site.register(Assignment)
admin.site.register(Report)
admin.site.register(Recipe)
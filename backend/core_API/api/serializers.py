from rest_framework import serializers
from api.models.admin.model import Admin
from api.models.user.model import User
from api.models.doctor.model import Doctor
from api.models.user_support.model import UserSupport
from api.models.assignment.model import Assignment
from api.models.report.model import Report
from api.models.recipe.model import Recipe

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = (
            'id',
            'email',
            'password',
            'active'
        )

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = (
            'id',
            'email',
            'password',
            'dni',
            'photo',
            'name',
            'firstSurname',
            'secondSurname',
            'phoneNumber',
            'active'
        )
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'password',
            'photo',
            'name',
            'firstSurname',
            'secondSurname',
            'phoneNumber',
            'healthCardCode',
            'birthDate',
            'gender',
            'dni',
            'address',
            'postalCode',
            'active'
        )

class UserSupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSupport
        fields = (
            'id',
            'email',
            'password',
            'name',
            'firstSurname',
            'secondSurname',
            'phoneNumber',
            'active'
        )

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = (
            'id',
            'doctorId',
            'userId',
            'dateCreated',
            'active'
        )

    
class ReportSerializer(serializers.ModelSerializer):
    class meta:
        model = Report
        fields = (
            'id',
            'doctorId',
            'userId',
            'reportInfo',
            'dateCreated'
        )
    
class RecipeSerializer(serializers.ModelSerializer):
    class meta:
        model = Recipe
        fields = (
            'id',
            'doctorId',
            'userId',
            'reportId',
            'medicine',
            'dateCreated'
        )
from rest_framework import serializers
from api.models import Admin,Doctor,User,UserSupport,Assignment,Report,Recipe

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
    model = Assignment
    fields = (
        'id',
        'doctorId',
        'userId',
        'dateCreated'
    )
    
class ReportSerializer(serializers.ModelSerializer):
    model = Report
    fields = (
        'id',
        'doctorId',
        'userId',
        'reportInfo',
        'dateCreated'
    )
    
class RecipeSerializer(serializers.ModelSerializer):
    model = Recipe
    fields = (
        'id',
        'doctorId',
        'userId',
        'reportId',
        'medicine',
        'dateCreated'
    )
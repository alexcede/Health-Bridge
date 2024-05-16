from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .model import Admin
from .serializer import AdminSerializer

from django.core.exceptions import ValidationError
from api.fields_validator import validate_unique_fields


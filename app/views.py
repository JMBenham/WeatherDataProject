"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from app.models import Student, WeatherData
from app.serializers import StudentSerializer, WeatherDataSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return JSONResponse(serializer.data)

@csrf_exempt
def weather_data_list(request):
    if request.method == 'GET':
        weather = WeatherData.objects.all()
        serializer = WeatherDataSerializer(weather, many=True)
        return JSONResponse(serializer.data)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = WeatherDataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def get_student(request, id):
    try:
        student = Student.objects.get(student_number = id)
    except Student.DoesNotExist:
        return HttpResponse(status = 404)

    if request.method == "GET":
        serializer = StudentSerializer(student)
        return JSONResponse(serializer.data)

    

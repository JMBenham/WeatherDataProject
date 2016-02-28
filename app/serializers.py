from app.models import Student, WeatherData
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('pk', 'first_name', 'last_name', 'location', 'student_number')

class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = ('temperature', 'student')
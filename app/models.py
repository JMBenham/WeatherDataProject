"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Student(models.Model):
    def __unicode__(self):
        if self.first_name and self.last_name:
            return unicode(self.first_name) + u" " +unicode(self.last_name)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50)

class WeatherData(models.Model):
    def __unicode__(self):
        if self.student:
            return unicode(self.student) + u", " + unicode(self.temperature)
    class Meta:
        verbose_name_plural = "Weather Data"
    temperature = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)




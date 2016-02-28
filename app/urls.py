from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^students/$', views.student_list),
    url(r'^weatherdata/$', views.weather_data_list),
    url(r'^students/(?P<id>[0-9]+)/$', views.get_student),
    ]
from django.urls import path

from . import views

urlpatterns = [
    path('dataloggers/',
         views.dataloggers_view, name='dataloggers'),
    path('dataloggers/detail/<slug:slug>',
         views.sensor_detail, name='sensor_detail'),
    path('dataloggers/api/data/<slug:slug>',
         views.api_add_data, name='sensor_add_data'),


]

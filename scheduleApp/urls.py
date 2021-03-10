from django.urls import path
from .views import *

urlpatterns = [
    path('api/timing_data/', allData.as_view(),name='timing_data'),
    path('api/timimg_edit/<int:pk>',action.as_view(), name='timimg_edit'),
    path('api/doctordata/',doctordata.as_view(),name="doctor_data"),
    path('api/doctoredit/<int:pk>',doctoredit.as_view(),name="doctor_edit")
]
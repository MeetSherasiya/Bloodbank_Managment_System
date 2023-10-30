from django.urls import path
from patient.views import *

urlpatterns = [
    path('', dashboard, name="patient-dashboard"),
    path('login/', loginPatient, name="patient-login"),
    path('logout/', logoutPatient, name="logout"),
    path('register/', register, name="patient-register"),
    path('blood-request/', blood_request, name="blood-request"),
    path('blood-history/', blood_request_history, name="blood-history"),
]
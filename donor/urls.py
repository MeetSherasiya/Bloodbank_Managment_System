from django.urls import path
from donor.views import *

urlpatterns = [
    # path('', dashboard, name="donor-dashboard"),
    path('register/', register, name="donor-register"),
    path('blood-request/', blood_request, name="donor-blood-request"),
    path('blood-history/', blood_request_history, name="donor-blood-history"),
]
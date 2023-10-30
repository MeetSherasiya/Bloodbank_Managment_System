from django.urls import path
from bank.views import *

urlpatterns = [
    path('pending_request/', pending_request_patient, name="pending_request_patient"),
    path('pending_request_aprroved/<str:created>/', approved_request_patient, name="approved_request_patient"),
    path('pending_request_reject/<str:created>/', reject_request_patient, name="reject_request_patient"),
    path('history_request/', history_request_patient, name="history_request_patient"),
    path('pateint_details/', pateint_details, name="pateint_details"),
    path('edit_blood_request/<int:request_id>/', edit_blood_request, name='edit_blood_request'),
    path('delete_blood_request/<int:request_id>/', delete_blood_request, name='delete_blood_request'),
    path('pending_request_donor/', pending_request_donor, name="pending_request_donor"),
    path('history_request_donor/', history_request_donor, name="history_request_donor"),
    path('pending_request_aprroved_donor/<str:created>/', approved_request_donor, name="approved_request_donor"),
    path('pending_request_reject_donor/<str:created>/', reject_request_donor, name="reject_request_donor"),
    path('edit_blood_donate_request/<int:request_id>/', edit_blood_donate_request, name='edit_blood_donate_request'),
    path('delete_blood_donor_request/<int:request_id>/', delete_blood_donor_request, name='delete_blood_donor_request'),
    path('donor_details/', donor_details, name="donor_details"),
]


from django import forms
from patient.models import BloodRequest

class BloodRequestForm(forms.ModelForm):
    class Meta:
        model = BloodRequest
        fields = ['patient_name', 'patient_age', 'reason', 'bloodgroup', 'unit']
        widgets = {
                'user': forms.HiddenInput(),
            }

class AdminBloodRequestForm(forms.ModelForm):
    class Meta:
        model = BloodRequest
        fields = ['patient_name', 'patient_age', 'reason', 'bloodgroup', 'unit', 'progress']
        widgets = {
                'user': forms.HiddenInput(),
            }
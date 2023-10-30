from django import forms
from donor.models import BloodDonate

class BloodDonateForm(forms.ModelForm):
    class Meta:
        model = BloodDonate
        fields = ['patient_name', 'patient_age', 'disease', 'bloodgroup', 'unit']
        widgets = {
                'user': forms.HiddenInput(),
            }

class AdminBloodDonateForm(forms.ModelForm):
    class Meta:
        model = BloodDonate
        fields = ['patient_name', 'patient_age', 'disease', 'bloodgroup', 'unit', 'progress']
        widgets = {
                'user': forms.HiddenInput(),
            }
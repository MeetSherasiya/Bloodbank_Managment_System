from django.shortcuts import render, redirect
from patient.models import BloodRequest
from donor.models import BloodDonate
from patient.forms import AdminBloodRequestForm
from donor.forms import AdminBloodDonateForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group
from account.models import CustomUser
from bank.models import Blood

# Create your views here.
def pending_request_patient(request):
    history = BloodRequest.objects.filter(progress = 'Pending').order_by('-id')
    return render(request, 'admin/patient/pending_history.html', {'historys': history})

def approved_request_patient(request, created):
    blood_request = get_object_or_404(BloodRequest, id=created)

    blood = get_object_or_404(Blood, name = blood_request.bloodgroup)
    if blood.unit >= blood_request.unit:
        blood.unit -= blood_request.unit
        blood.save()
    else:
        messages.warning(request, 'Not Sufficient Blood is not available is Blood Bank.')
        return redirect('pending_request_patient')

    # Update the progress attribute
    blood_request.progress = "Approved"
    blood_request.save()
    messages.success(request, 'Request is Approved')
    return redirect('pending_request_patient')

def reject_request_patient(request, created):
    blood_request = get_object_or_404(BloodRequest, id=created)

    # Update the progress attribute
    blood_request.progress = "Reject"
    blood_request.save()
    messages.warning(request, 'Request is Reject')
    return redirect('pending_request_patient')

def history_request_patient(request):
    history = BloodRequest.objects.all().order_by('-id')
    return render(request, 'admin/patient/history.html', {'historys': history})

def pateint_details(request):
    patient_group = Group.objects.get(name='Patient')
    patient_requests = CustomUser.objects.filter(groups=patient_group).order_by('-id')
    return render(request, 'admin/patient/patient_details.html', {'historys': patient_requests})


def edit_blood_request(request, request_id):
    blood_request = get_object_or_404(BloodRequest, id=request_id)
    bloodGroup = ['O+','O-','A+','A-','B+','B-','AB+','AB-']
    Progress = ["Pending", "Approved", "Reject"]
    if request.method == "POST":
        form = AdminBloodRequestForm(request.POST, instance=blood_request)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blood request updated successfully.')
            return redirect('history_request_patient')
    else:
        form = AdminBloodRequestForm(instance=blood_request)

    return render(request, 'admin/patient/edit_blood_request.html', {'form': form, 'bloodGroup': bloodGroup, 'progress': Progress})

def delete_blood_request(request, request_id):
    blood_request = get_object_or_404(BloodRequest, id=request_id)
    blood_request.delete()
    messages.success(request, 'Blood request Delete successfully.')
    return redirect('history_request_patient')


def pending_request_donor(request):
    history = BloodDonate.objects.filter(progress = 'Pending').order_by('-id')
    return render(request, 'admin/donor/pending_history.html', {'historys': history})


def history_request_donor(request):
    history = BloodDonate.objects.all().order_by('-id')
    return render(request, 'admin/donor/history.html', {'historys': history})

def approved_request_donor(request, created):
    blood_request = get_object_or_404(BloodDonate, id=created)

    # Update the progress attribute
    blood_request.progress = "Approved"
    blood_request.save()
    blood = get_object_or_404(Blood, name = blood_request.bloodgroup)
    blood.unit += blood_request.unit
    blood.save()
    messages.success(request, 'Request is Approved')
    return redirect('pending_request_donor')

def reject_request_donor(request, created):
    blood_request = get_object_or_404(BloodDonate, id=created)

    # Update the progress attribute
    blood_request.progress = "Reject"
    blood_request.save()
    messages.warning(request, 'Request is Reject')
    return redirect('pending_request_donor')


def edit_blood_donate_request(request, request_id):
    blood_request = get_object_or_404(BloodDonate, id=request_id)
    bloodGroup = ['O+','O-','A+','A-','B+','B-','AB+','AB-']
    Progress = ["Pending", "Approved", "Reject"]
    if request.method == "POST":
        form = AdminBloodDonateForm(request.POST, instance=blood_request)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blood request updated successfully.')
            return redirect('history_request_donor')
    else:
        form = AdminBloodDonateForm(instance=blood_request)

    return render(request, 'admin/donor/edit_blood_request.html', {'form': form, 'bloodGroup': bloodGroup, 'progress': Progress})

def delete_blood_donor_request(request, request_id):
    blood_request = get_object_or_404(BloodDonate, id=request_id)
    blood_request.delete()
    messages.success(request, 'Blood request Delete successfully.')
    return redirect('history_request_donor')

def donor_details(request):
    patient_group = Group.objects.get(name='Donor')
    patient_requests = CustomUser.objects.filter(groups=patient_group).order_by('-id')
    return render(request, 'admin/donor/donor_details.html', {'historys': patient_requests})

from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from account.forms import UserAdminCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from donor.forms import BloodDonateForm
from donor.models import BloodDonate

def register(request):
    form = UserAdminCreationForm()
    if request.method == 'POST':
        form = UserAdminCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            # Add user to the "patient" group
            group = Group.objects.get(name='Donor')
            user.groups.add(group)
            messages.success(request, 'Donor Added Successfully')
            return redirect('patient-login')

    return render(request, 'donor/register.html', {'form': form})


@login_required
def blood_request(request):
    bloodGroup = ['O+','O-','A+','A-','B+','B-','AB+','AB-']
    if request.method == "POST":
        form = BloodDonateForm(request.POST)
        if form.is_valid():
            # Assign the logged-in user to the form before saving
            form.instance.user = request.user
            form.save()
            messages.success(request, 'Donate Blood Request is Create Successfully')
    else:
        form = BloodDonateForm()

    return render(request, 'donor/blood_request.html', {'form': form, 'bloodGroup': bloodGroup})


@login_required
def blood_request_history(request):
    history = BloodDonate.objects.filter(user_id = request.user).order_by('-created_at')
    return render(request, 'donor/blood_history.html', {'historys': history})

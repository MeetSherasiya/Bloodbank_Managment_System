from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from account.forms import UserAdminCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from patient.forms import BloodRequestForm
from patient.models import BloodRequest
from donor.models import BloodDonate
from bank.models import Blood

# Create your views here.
def loginPatient(request):
    logout(request)
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username = email, password=password)

        if user is not None:
            login(request, user)
            if user.is_superuser or user.is_staff:
                messages.success(request,'Admin Login Successfully')
                return redirect('patient-dashboard')
            else:
                messages.success(request,'Login Successfully')
                next_url = request.GET.get('next', '/')

                # Ensure 'next' URL ends with a trailing slash
                if not next_url.endswith('/'):
                    next_url += '/'

                return redirect(next_url)
        else:
            messages.warning(request, 'Please Enter User Details Properly')

    return render(request, 'patient/login.html')

def register(request):
    form = UserAdminCreationForm()
    if request.method == 'POST':
        form = UserAdminCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            # Add user to the "patient" group
            group = Group.objects.get(name='Patient')
            user.groups.add(group)
            messages.success(request, 'User Added Successfully')
            return redirect('patient-login')

    return render(request, 'patient/register.html', {'form': form})

def logoutPatient(request):
    logout(request)
    messages.success(request, "Logout Successfully")
    return redirect('patient-login')


@login_required
def dashboard(request):
    total = BloodRequest.objects.filter(user_id = request.user).count()
    Pending = BloodRequest.objects.filter(progress="Pending", user_id = request.user).count()
    Approved = BloodRequest.objects.filter(progress="Approved", user_id = request.user).count()
    Reject = BloodRequest.objects.filter(progress="Reject", user_id = request.user).count()
    history = BloodRequest.objects.filter(user_id = request.user).order_by('-created_at')[:10]
    donor_total = BloodDonate.objects.filter(user_id = request.user).count()
    donor_Pending = BloodDonate.objects.filter(progress="Pending", user_id = request.user).count()
    donor_Approved = BloodDonate.objects.filter(progress="Approved", user_id = request.user).count()
    donor_Reject = BloodDonate.objects.filter(progress="Reject", user_id = request.user).count()
    donate = BloodDonate.objects.filter(user_id = request.user).order_by('-created_at')[:10]
    blood = Blood.objects.all()
    context = {'historys': history,
               'total': total,
               'Pending': Pending,
               'Approved': Approved,
               'Reject': Reject,
               'Donate': donate,
               'donor_total': donor_total,
               'donor_Pending': donor_Pending,
               'donor_Approved': donor_Approved,
               'donor_Reject': donor_Reject,
               'Bloods': blood
               }
    return render(request, 'patient/dashboard.html', context)

@login_required
def blood_request(request):
    bloodGroup = ['O+','O-','A+','A-','B+','B-','AB+','AB-']
    if request.method == "POST":
        form = BloodRequestForm(request.POST)
        if form.is_valid():
            # Assign the logged-in user to the form before saving
            form.instance.user = request.user
            form.save()
            messages.success(request, 'Request is Create Successfully')
    else:
        form = BloodRequestForm()

    return render(request, 'patient/blood_request.html', {'form': form, 'bloodGroup': bloodGroup})

@login_required
def blood_request_history(request):
    history = BloodRequest.objects.filter(user_id = request.user).order_by('-created_at')
    return render(request, 'patient/blood_history.html', {'historys': history})


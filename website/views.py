from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import doctor,availability

# Create your views here.
@login_required
def home(request):
    di = {'title':'Dashboard'}
    if doctor.objects.filter(user=request.user).exists():
        di['doctor']=True
        doc_ins = doctor.objects.filter(user=request.user).first()
        appoint = availability.objects.filter(doctor=doc_ins)
        di['appoint'] = appoint
        return render(request, "website/home.html", di)
    else:
        appoint = availability.objects.filter(user=request.user)
        di['appoint'] = appoint
        return render(request, "website/home.html", di)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.city = form.cleaned_data.get('city')
            user.profile.age = form.cleaned_data.get('age')
            user.profile.addrress = form.cleaned_data.get('addrress')
            user.profile.gender = form.cleaned_data.get('gender')
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'website/signup.html', {'form': form})

@login_required
def appointment(request):
    if request.method == 'POST':
        form = AddAppointmentForm(request.POST)
        if form.is_valid():
            doctor_ob = form.cleaned_data.get('doctor')
            date_ob = form.cleaned_data.get('date')
            time_ob = form.cleaned_data.get('time')
            appoint = availability(doctor=doctor_ob,user=request.user,date=date_ob,time=time_ob)
            appoint.save()
            return redirect('home')
    else:
        form = AddAppointmentForm()
    return render(request, 'website/appoint.html', {'form': form})
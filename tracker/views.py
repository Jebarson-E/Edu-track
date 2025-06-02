from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth import authenticate, login, logout # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from django.contrib.auth.forms import UserCreationForm # type: ignore
from django.contrib import messages # type: ignore
from .forms import StudentForm, AttendanceForm, MarkForm, BehaviorForm
from .models import *

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'tracker/login.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'tracker/register.html', {'form': form})

@login_required
def home(request):
    return render(request, 'tracker/home.html')

@login_required
def add_student(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'tracker/form.html', {'form': form, 'title': 'Add Student'})


@login_required
def record_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            student_name = form.cleaned_data['student_name']
            date = form.cleaned_data['date']
            present = form.cleaned_data['present']

            try:
                # ✅ Prevent duplicate entries – update if already exists
                Attendance.objects.update_or_create(
                    student_name=student_name,
                    date=date,
                    defaults={'present': present}
                )
                return redirect('home')
            except Exception as e:
                print(f"Error saving attendance: {e}")
                print(f"Student name: {student_name}, Date: {date}, Present: {present}")
        else:
            print("Form errors:", form.errors)
    else:
        form = AttendanceForm()

    return render(request, 'tracker/form.html', {'form': form, 'title': 'Record Attendance'})

@login_required
def record_marks(request):
    form = MarkForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'tracker/form.html', {'form': form, 'title': 'Record Marks'})

@login_required
def record_behavior(request):
    form = BehaviorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'tracker/form.html', {'form': form, 'title': 'Record Behavior'})

@login_required
def reports(request):
    students = Student.objects.all()
    attendance = Attendance.objects.all()
    marks = Mark.objects.all()
    behavior = Behavior.objects.all()
    return render(request, 'tracker/reports.html', {
        'students': students,
        'attendance': attendance,
        'marks': marks,
        'behavior': behavior,
    })

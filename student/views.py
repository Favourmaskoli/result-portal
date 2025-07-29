from django.shortcuts import render
from student.forms import StudentProfileForm
from student.models import Student
from django.shortcuts import redirect, get_object_or_404
from result.models import Term, Session
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required
def index(request):
    """
    Render the student portal index page.
    """
    student = Student.objects.filter(user=request.user).first()
    if not student:
        return redirect('student:student_profile')
    print(student.school)
    return render(request, 'student/index.html', {'student': student})

@login_required
def create_student_profile(request):
    """
    Create a student profile if it does not exist.
    """
    try:
        student = Student.objects.get(user=request.user)
        return redirect('student:update_profile')
    except Student.DoesNotExist:
        pass

    if request.method == 'POST':
        form = StudentProfileForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = request.user
            student.save()
            return render(request, 'student/profile.html', {'form': form, 'success': True, 'student': student})
    else:
        form = StudentProfileForm()
    return render(request, 'student/profile.html', {'form': form, 'student': student})

def update_student(request):
    """update student profile"""
    student = get_object_or_404(Student, user=request.user)
    if request.method == "POST":
        form = StudentProfileForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('student:student_profile')
    else:
        form = StudentProfileForm(instance=student)
    return render(request, 'student/profile.html', {'form': form, 'student': student})

@login_required
def results(request):
    """
    Render the student results page.
    """
    return render(request, 'student/results.html', {} )

@login_required
def tasks(request):
    """
    Render the student tasks page.
    """
    return render(request, 'student/tasks.html', {} )

@login_required
def logout_view(request):
    """
    Handle student logout.
    """
    return render(request, 'student/logout.html', {} )

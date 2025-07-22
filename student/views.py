from django.shortcuts import render
from student.forms import StudentProfileForm
from student.models import Student
from django.shortcuts import redirect
from result.models import Term, Session
from django.contrib.auth.decorators import login_required

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

# def profile(request):
#     """
#     Render the student profile page.
#     """
#     student = request.user.student if hasattr(request.user, 'student') else None
#     form = StudentProfileForm(request.POST, instance=request.user)
#     if request.method == 'POST':
#         form = StudentProfileForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return render(request, 'student/profile.html', {'form': form, 'success': True})
#     return render(request, 'student/profile.html', {'form': form})

@login_required
def create_student_profile(request):
    """
    Create a student profile if it does not exist.
    """
    student = Student.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = StudentProfileForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = request.user
            student.save()
            return render(request, 'student/profile.html', {'form': form, 'success': True, 'student': student})
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

@login_required
def result_details(request):
    """
    Render the student result details page.
    """
    terms = Term.objects.all()
    sessions = Session.objects.all()

    context = {
        'terms': terms,
        'sessions': sessions
    }
    return render(request, 'student/results.html', context)

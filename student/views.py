from django.shortcuts import render

# Create your views here.
def index(request):
    """
    Render the student portal index page.
    """
    return render(request, 'student/index.html', {} )

def profile(request):
    """
    Render the student profile page.
    """
    return render(request, 'student/profile.html', {} )

def results(request):
    """
    Render the student results page.
    """
    return render(request, 'student/results.html', {} )

def tasks(request):
    """
    Render the student tasks page.
    """
    return render(request, 'student/tasks.html', {} )

def logout_view(request):
    """
    Handle student logout.
    """
    return render(request, 'student/logout.html', {} )


def result_details(request):
    """
    Render the student result details page.
    """
    return render(request, 'student/result.html', {})
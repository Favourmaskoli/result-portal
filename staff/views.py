from django.shortcuts import render, redirect, get_list_or_404
from staff.models import Staff
from django.contrib.auth.decorators import login_required
from staff.forms import ResultsUploadForm
from django.contrib import messages
from student.models import Student

# Create your views here.

@login_required
def staff_dashboard(request):
    user = request.user
    if request.user.is_staff:
        staff = Staff.objects.filter(user=user).first()
    if request.user.is_superuser:
        user = user
    context = {
        'staff': staff,
        'user':user,
        'students': Student.objects.all()
    }
    return render(request, 'staff/staff_dashboard.html', context)

@login_required
def upload_result(request):
    """Upload students result"""
    # student = get_list_or_404()
    if request.method=='POST':
        form = ResultsUploadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Result uploaded successfully')
        return redirect('staff:upload_result')
    else:
        form = ResultsUploadForm()
    context = {
        'form': form,
        'students': Student.objects.all()
    }

    return render(request, 'staff/upload_result.html', context)

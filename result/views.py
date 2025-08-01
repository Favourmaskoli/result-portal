from django.shortcuts import render, redirect
from result.models import Result
from django.views.generic import DetailView, ListView
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from school.models import Session, Term
from decimal import Decimal
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML

# def index(request):
#     return render(request, 'result/index.html')


class ResultSearch(ListView):
    model = Result
    context_object_name = 'results'
    template_name = 'student/results_display.html'

    def get_queryset(self):
        student = self.request.user.student_profile
        term_id = self.request.GET.get('term')
        session_id = self.request.GET.get('session')
        queryset = Result.objects.filter(student=student)
        if term_id:
            queryset = queryset.filter(term_id=term_id)
            print(queryset)
        if session_id:
            queryset = queryset.filter(session_id=session_id)
            print(queryset)
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['term'] = self.request.GET.get('term')
        context['session'] = self.request.GET.get('session')
        return context
    
def results_percentage(total, obtained):
    if total:
        return round((obtained/total)*100, 2)
    return 0

def get_grade_remark(percentage):
    if percentage >= 70:
        return "A", "Excellent"
    if percentage >= 60:
        return "B", "Very Good"
    if percentage >= 50:
        return "C", "Good"
    if percentage >= 45:
        return "D", "Fair"
    if percentage >= 40:
        return "E", "Pass"
    else:
        return "F", "Fail"


@login_required    
def result_detail(request):
    """
    Show a detail view of student results for selected term and session
    """
    term_id = request.GET.get('term')
    session_id = request.GET.get('session')
    student = request.user.student_profile

    if not term_id or not session_id:
        return redirect('result:result')
    results = Result.objects.filter(student=student, term_id=term_id, session_id=session_id)
    # for result in results:
    #     subject = result.subject
    #     subject_grade, subject_remark = result.grade()
    total_marks_obtained = sum([result.mark_obtained for result in results], Decimal("0.00"))
    total_marks_expected = sum([result.subject.total_marks for result in results], Decimal("0.00"))
    percentage = results_percentage(total_marks_expected, total_marks_obtained)
    grade, remark = get_grade_remark(percentage)

    context = {
        'results': results,
        'term': Term.objects.filter(id=term_id).first(),
        'session': Session.objects.filter(id=session_id).first(),
        'result_grade': grade,
        'result_remark': remark,
        # 'subject_grade': subject_grade,
        # 'subject_remark': subject_remark,
        'score_percentage': percentage,
        # 'subject': subject,
        'total_marks_obtained': total_marks_obtained,
    }
    return render(request, 'student/result.html', context)


@login_required
def result(request):
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

@login_required
def download_result_pdf(request):
    term = request.GET.get('term')
    session = request.GET.get('session')

    student = request.user.student_profile

    if not term or not session:
        return HttpResponse('No result found for the term and session')

    results = Result.objects.filter(student=student, term_id=term, session_id=session)

    if not results.exists():
        return HttpResponse('No results found for the term and session')

    total_marks_obtained = sum([result.mark_obtained for result in results], Decimal("0.00"))
    total_marks_expected = sum([result.subject.total_marks for result in results], Decimal("0.00"))
    percentage = results_percentage(total_marks_expected, total_marks_obtained)
    grade, remark = get_grade_remark(percentage)

    term_obj = Term.objects.filter(id=term).first()
    session_obj = Session.objects.filter(id=session).first()

    html_string = render_to_string('student/result.html', {
        'results': results,
        'term': term_obj,
        'session': session_obj,
        'result_grade': grade,
        'result_remark': remark,
        'score_percentage': percentage,
        'total_marks_obtained': total_marks_obtained,
    })

    pdf_file = HTML(string=html_string, base_url=request.build_absolute_uri()).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    return response

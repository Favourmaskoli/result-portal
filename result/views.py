from django.shortcuts import render

def index(request):
    return render(request, 'result/index.html')

# def result_details(request):
#     """
#     Render the result details page.
#     """
#     return render(request, 'result/result_details.html', {})

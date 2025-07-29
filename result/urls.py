from django.urls import path
from result.views import ResultSearch, result, result_detail


app_name = 'result'
urlpatterns = [
    path('search', ResultSearch.as_view(), name='searchResult'),
    path('result/', result, name='result'),
    path('result_detail', result_detail, name='result_detail')
]

from django.urls import path
from result.views import index, ResultSearch, result, result_detail


app_name = 'result'
urlpatterns = [
    path('', index, name='index'),
    path('search', ResultSearch.as_view(), name='searchResult'),
    path('result/', result, name='result'),
    path('result_detail', result_detail, name='result_detail')
]

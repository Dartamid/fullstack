from django.urls import path
from .views import title_view, vacancies

urlpatterns = [
    path('', title_view, name='title_page'),
    path('last_vacancies/', vacancies, name='last_vacancies')
]
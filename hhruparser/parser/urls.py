from django.urls import path
from .views import title_view, vacancies, skills_view, geography_view

urlpatterns = [
    path('', title_view, name='title_page'),
    path('last_vacancies/', vacancies, name='last_vacancies'),
    path('skills/', skills_view, name='skills_list'),
    path('geography', geography_view, name='geography')
]
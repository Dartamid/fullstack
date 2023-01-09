from django.shortcuts import render
from .models import Vacancy
from .utils import add_vacancies

# Create your views here.
def title_view(request):
    return render(
        request, 
        'title_page.html', 
    )

def vacancies(request):
    add_vacancies()
    vacancies = Vacancy.objects.all()[:10]
    return render(
        request,
        'vacancies.html',
        context={
            'vacancies': vacancies,
        }
    )
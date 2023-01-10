from django.shortcuts import render
from .models import Vacancy, Homepage
from .utils import add_vacancies

# Create your views here.
def title_view(request):
    try: homepage = Homepage.objects.all()[0]
    except: homepage = None
    return render(
        request, 
        'title_page.html',
        context={
            'homepage': homepage
        } 
    )

def vacancies(request):
    #add_vacancies()
    vacancies = Vacancy.objects.all()[:10]
    return render(
        request,
        'vacancies.html',
        context={
            'vacancies': vacancies,
        }
    )
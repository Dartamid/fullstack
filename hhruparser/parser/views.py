from django.shortcuts import render
from .models import Vacancy, Homepage, Skills, Geography
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
    
def skills_view(request):
    skills = Skills.objects.all()[:20]
    return render(
        request,
        'skills.html',
        context={
            'skills': skills,
        }
    )
    
def geography_view(request):
    geography = Geography.objects.all()[0]
    return render(
        request,
        'geography.html',
        context={
            'geography': geography,
        }
    )
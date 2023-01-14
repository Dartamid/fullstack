from django.shortcuts import render
from .models import Vacancy, Homepage, Skills, Geography, Demand, SkillsPlot
from .utils import add_vacancies


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
    add_vacancies()
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
    plot = SkillsPlot.objects.all()[0]
    return render(
        request,
        'skills.html',
        context={
            'skills': skills,
            'plot': plot,
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
    
def demand_view(request):
    demand = Demand.objects.all()[0]
    return render(
        request,
        'demand.html',
        context={
            'demand': demand,
        }
    )
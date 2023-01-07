from django.shortcuts import render
from .models import Vacancy

# Create your views here.
def title_view(request):
    return render(
        request, 
        'title_page.html', 
    )


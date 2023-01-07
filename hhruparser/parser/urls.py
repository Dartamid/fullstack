from django.urls import path
from .views import title_view

urlpatterns = [
    path('', title_view, name='title_page'),
]
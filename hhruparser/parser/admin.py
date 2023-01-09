from django.contrib import admin
from .models import Vacancy, Geography, Skills, Demand

# Register your models here.
@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('pk', 'hh_id', 'name',)


@admin.register(Geography)
class Geography(admin.ModelAdmin):
    list_display = ('pk',)
    

@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('pk',)
    
    
@admin.register(Demand)
class DemandAdmin(admin.ModelAdmin):
    list_display = ('pk',)
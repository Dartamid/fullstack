from django.contrib import admin
from .models import Vacancy, Geography, Skills, Demand, Homepage, SkillsPlot

# Register your models here.
@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('pk', 'hh_id', 'name',)

@admin.register(Homepage)
class HomepageAdmin(admin.ModelAdmin):
    list_display = ('pk',)


@admin.register(Geography)
class Geography(admin.ModelAdmin):
    list_display = ('pk',)
    

@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('year',)
    
    
@admin.register(Demand)
class DemandAdmin(admin.ModelAdmin):
    list_display = ('pk',)
    
    
@admin.register(SkillsPlot)
class SkillsPlotAdmin(admin.ModelAdmin):
    list_display = ('pk',)
    
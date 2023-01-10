from django.db import models

# Create your models here.
class Vacancy(models.Model):
    hh_id = models.CharField(
        max_length=64,
        verbose_name='ID на hh.ru'
    )
    name = models.CharField(
        max_length=64,
        verbose_name='Название вакансии'
    )
    description = models.TextField(verbose_name='Описание')
    employer = models.CharField(
        verbose_name='Компания',
        max_length=64
    )
    salary = models.CharField(
        verbose_name='Оклад',
        max_length=64,
        blank=True, null=True
    )
    key_skills = models.TextField(
        verbose_name='Навыки',
        blank=True, null=True,
    )
    area = models.CharField(
        verbose_name='Регион',
        max_length=64,
        blank=True, null=True
    )
    url = models.URLField(
        blank=True, null=True,
        max_length=150,
    )
    published_at = models.DateTimeField(verbose_name='Дата публикации вакансии')    

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"
        ordering = ('-published_at',)

    def __str__(self):
        return self.name
    
    def get_list_skills(self):
        return self.key_skills.split(', ')
    
    
class Homepage(models.Model):
    description = models.TextField(
        blank=True, null=True,
        verbose_name='Описание профессии'
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='homepage/'
    )
    
    class Meta:
        verbose_name = 'Главная страница'
        
        
class Geography(models.Model):
    text = models.TextField(
        blank=True, null=True,
        verbose_name='Текст подсказки'
    )
    table_salary = models.TextField(
        blank=True, null=True,
        verbose_name='Статистика зарплаты по городам'
    )
    table_dist = models.TextField(
        blank=True, null=True,
        verbose_name='Статистика распределения вакансий по городам'
    )
    
    class Meta:
        verbose_name = ('География вакансий')


class Skills(models.Model):
    text = models.TextField(
        blank=True, null=True,
        verbose_name='Текст подсказки',
    )
    table_skills = models.TextField(
        blank=True, null=True,
        verbose_name='Таблица скиллов по городам'
    )
    
    class Meta:
        verbose_name = ('Навыки по годам')
    
    def __str__(self):
        return self.table_skills
    
    
class Demand(models.Model):
    dynamic_salary = models.ImageField(
        verbose_name='Динамика зарплат по годам',
        upload_to='demand/'
    )
    dynamic_count_prof = models.ImageField(
        verbose_name='Динамика количества заданной вакансий',
        upload_to='demand/'
    )
    dynamic_count_it = models.ImageField(
        verbose_name='Динамика количества IT вакансий'
    )
    
    class Meta:
        verbose_name = ('Восстребованность профессии')
    
    
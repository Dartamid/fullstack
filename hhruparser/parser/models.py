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
    desription = models.TextField(verbose_name='Описание')
    skills = models.TextField(
        verbose_name='Навыки',
        blank=True, null=True
    )
    employer = models.CharField(
        verbose_name='Компания',
        max_length=64
    )
    salary = models.CharField(
        verbose_name='Оклад',
        max_length=64,
        blank=True, null=True
    )
    area = models.CharField(
        verbose_name='Регион',
        max_length=64,
        blank=True, null=True
    )
    published_at = models.DateTimeField(verbose_name='Дата публикации вакансии')    

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"
        ordering = ('-published_at',)

    def __str__(self):
        return self.name

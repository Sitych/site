from django.db import models
from django.forms import ModelForm
from django import forms
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns

ac = "Меропритятие"
pr = "Задача"
f_n = "Имя"
s_n = "Фамилия"
t_n = "Отчество"
numb = "Номер"
info = "Описание"
i_n = "ИНН"
web_url = "Адрес сайта"
s_s = "Краткое описание"


class Problem(models.Model):
    goal = models.TextField(pr, max_length=1000, help_text="Введите задачу и опишите ее")
    first_name = models.CharField(f_n, max_length=200, help_text="Назначить ответственного", blank=True)
    second_name = models.CharField(s_n, max_length=200, blank=True)
    third_name = models.CharField(t_n, max_length=200, blank=True)
    need_time = models.DateField(verbose_name="Дата")
    status = models.CharField('Статус выполнения', max_length=10, blank=True, default="Готово")

    def __str__(self):
        return self.goal

    class Meta:
        verbose_name = pr
        verbose_name_plural = "Задачи"


class Face(models.Model):
    FACE_CHOICES = (
        ('Юр. лицо', 'Юридическое лицо'),
    )
    name = models.CharField(max_length=20, choices=FACE_CHOICES, unique=True)

    def __str__(self):
        return self.name


class Face1(models.Model):
    FACE_CHOICES = (
        ('Физ. лицо', 'Физическое лицо'),
    )
    name = models.CharField(max_length=20, choices=FACE_CHOICES, unique=True)

    def __str__(self):
        return self.name


class Representative(models.Model):
    first_name = models.CharField(f_n, max_length=200, help_text="Имя")
    second_name = models.CharField(s_n, max_length=200, help_text="Фамилия")
    third_name = models.CharField(t_n, max_length=200, help_text="Отчество", blank=True)
    number = models.CharField(numb, max_length=200, help_text="Номер телефона в формате: +7 123-456-7890")
    email = models.EmailField(max_length=15, help_text="email адрес")

    class Meta:
        verbose_name = "Представитель"
        verbose_name_plural = "Представители"

    def __str__(self):
        return self.first_name + " " + self.second_name + " " + self.third_name


class Partner(models.Model):
    name = models.CharField('Название организации', max_length=50)
    identification_number = models.CharField(i_n, max_length=12)
    partner_url = models.URLField(web_url, max_length=100, blank=True)
    short_summary = models.CharField(s_s, max_length=100, blank=True)
    goal = models.ManyToManyField(Problem, verbose_name=pr)
    face = models.ForeignKey(Face, on_delete=models.CASCADE, verbose_name="")
    representative = models.ManyToManyField(Representative, verbose_name="Представители")
    contact_info = models.CharField(max_length=50,
                                    help_text="История взаимоотношений с партнером (когда и по какому каналу (e-mail, телефон, личная встреча и т.п.) мы ранее общались",
                                    verbose_name="Последняя связь")
    contact_feedback = models.TextField(max_length=1000, help_text="Чем закончилась встреча",
                                        verbose_name="Обратная связь")
    tag = models.CharField("Тэг", max_length=10, help_text="Введите тег не более 10 символов", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Партнер юр. лицо"
        verbose_name_plural = "Партнеры юр. лица"


class PartnerIndividual(models.Model):
    first_name = models.CharField(f_n, max_length=200, help_text="Имя")
    second_name = models.CharField(s_n, max_length=200, help_text="Фамилия")
    third_name = models.CharField(t_n, max_length=200, help_text="Отчество", blank=True)
    number = models.CharField(numb, max_length=200, help_text="Номер телефона в формате: +7 123-456-7890")
    email = models.EmailField(max_length=30, help_text="email адрес")
    short_summary = models.CharField(s_s, max_length=100, blank=True)
    goal = models.ManyToManyField(Problem, verbose_name="Задачи")
    face = models.ForeignKey(Face1, on_delete=models.CASCADE,verbose_name="")
    contact_info = models.CharField(max_length=50,
                                    help_text="История взаимоотношений с партнером (когда и по какому каналу (e-mail, телефон, личная встреча и т.п.) мы ранее общались",
                                    verbose_name="Последняя связь")
    contact_feedback = models.TextField(max_length=1000, help_text="Чем закончилась встреча",
                                        verbose_name="Обратная связь")
    tag = models.CharField("Тэг", max_length=10, help_text="Введите тег не более 10 символов", blank=True)

    def __str__(self):
        return self.first_name + " " + self.second_name + " " + self.third_name

    class Meta:
        verbose_name = "Партнер физ. лицо"
        verbose_name_plural = "Партнеры физ. лица"


class Action(models.Model):
    action_name = models.CharField(ac, max_length=200, help_text="Введите названия мероприятия")
    action_time = models.TimeField(default="00:00:00", verbose_name="Время")
    action_period = models.DateField(verbose_name="Дата")
    action_info = models.CharField(info, max_length=200, help_text="Введите краткое описание мероприятия")
    action_goals = models.ManyToManyField(Problem, verbose_name=ac)
    action_partner = models.ManyToManyField(Partner,  verbose_name="Партнеры")

    def __str__(self):
        return self.action_name

    class Meta:
        verbose_name = ac
        verbose_name_plural = "Мероприятия"
        ordering = ["-action_period"]

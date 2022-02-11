from statistics import mode
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser


class Department(models.Model):
    name = models.CharField(
        max_length=25,
        verbose_name="Название отдела",
    )

    class Meta:
        ordering = ["id"]
        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"

    def __str__(self):
        return self.name


class Master(AbstractUser):
    POST_CHOICES = [
        ("hod", "начальник отдела"),
        ("se", "инженер-программист"),
        ("sa", "системный администратор"),
        ("ps", "специалист по принтерам"),
    ]
    post = models.CharField(
        max_length=3,
        choices=POST_CHOICES,
        default="hod",
        blank=True,
        null=True,
        verbose_name="Должность специалиста",
    )
    is_working = models.BooleanField(default=True)

    class Meta:
        ordering = ["last_name"]
        verbose_name = "Специалист"
        verbose_name_plural = "Специалисты"

    def __str__(self):
        return self.last_name + " " + self.first_name + "  Должность: " + self.post


class Problems(models.Model):
    PROBLEM_CHOICES = [
        ("np", "проблема с сетью"),
        ("cp", "проблема с компьютером"),
        ("pp", "проблема с печатью"),
        ("ap", "другая проблема"),
    ]
    name = models.CharField(
        max_length=2,
        choices=PROBLEM_CHOICES,
        blank=True,
        default="ap",
        verbose_name="Название проблемы",
    )
    id_master = models.ForeignKey(
        Master,
        on_delete=models.CASCADE,
        verbose_name="Назначенный специалист"
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Проблема"
        verbose_name_plural = "Проблемы"

    def __str__(self):
        return self.name


class Ordering(models.Model):
    fio = models.CharField(
        max_length=60,
        verbose_name="ФИО офрмляющего заявку"
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        verbose_name="Из какого отдела заявка"
    )
    problems = models.ForeignKey(
        Problems,
        on_delete=models.CASCADE,
        verbose_name="Прорблема"
    )
    note = models.CharField(
        max_length=150,
        verbose_name="Дополнительное описание проблемы"
    )
    order_status = models.CharField(
        max_length=40,
        default="Заявка принята",
        verbose_name="Статус заявки"
    )

    class Meta:
        ordering = ["id"]
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return self.fio + " " + self.department + " " + self.problems
from django.db import models

from config.settings import AUTH_USER_MODEL


# Create your models here.


class Employee(models.Model):
    full_name = models.CharField(
        max_length=100,
        verbose_name="Ваше ФИО",
        help_text="Введите Ваше имя полностью в формате ФИО",
    )
    position = models.CharField(
        max_length=100, verbose_name="Должность", help_text="Укажите Вашу должность"
    )
    vacation_status = models.BooleanField(
        default=False, verbose_name="Статус сотрудника"
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"


class Task(models.Model):
    STATUS_DONE = "done"
    STATUS_IN_PROGRESS = "in_progress"
    STATUS_NOT_STARTED = "not_started"
    STATUS_CHOICES = [
        (STATUS_DONE, "Выполнено"),
        (STATUS_IN_PROGRESS, "В процессе"),
        (STATUS_NOT_STARTED, "Не начато"),
    ]
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, verbose_name="Сотрудник"
    )
    task_name = models.CharField(max_length=100, verbose_name="Название задачи")
    parent_task = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Родительская задача",
    )
    start_date = models.DateField(verbose_name="Дата начала выполнения задачи")
    end_date = models.DateField(verbose_name="Дата завершения выполнения задачи")
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default=STATUS_NOT_STARTED,
        verbose_name="Статус",
    )
    comments = models.TextField(
        null=True, blank=True, verbose_name="Комментарий к задаче"
    )
    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Создатель",
    )
    is_active = models.BooleanField(
        default=True, verbose_name="Признак активности задачи"
    )
    is_important = models.BooleanField(
        default=False, verbose_name="Признак важности задачи"
    )

    def __str__(self):
        return f"{self.task_name}:{self.status}"

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

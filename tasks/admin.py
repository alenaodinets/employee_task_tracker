from django.contrib import admin

from tasks.models import Employee, Task


# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "full_name",
        "position",
        "vacation_status",
    )
    list_filter = ("vacation_status",)
    search_fields = ("full_name",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "task_name",
        "employee",
        "parent_task",
        "start_date",
        "end_date",
        "status",
        "comments",
        "owner",
    )
    list_filter = ("employee",)
    search_fields = ("task_name",)

"""Django admin configuration for the API application."""

from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Admin interface settings for the Task model."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)

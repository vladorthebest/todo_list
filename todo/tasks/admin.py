from django.contrib import admin
from tasks.models import *
# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass

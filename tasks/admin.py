from django.contrib import admin
from tasks.models import *
# Register your models here.


class TasksAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']
    search_fields = ['title']

    fieldsets = (
      ('Standard info', {
          'fields': ('title', ),
          'description': 'About task'
      }),
      ('Status info', {
          'fields': ('status', ),
          'classes': ['collapse']
      }),
   )


admin.site.register(Task, TasksAdmin)


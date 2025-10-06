from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import WorkOrder
@admin.register(WorkOrder)
class WorkOrderAdmin(admin.ModelAdmin):
    list_display = ("id","title","customer","status","priority","assigned_to","due_date","total_hours","total_cost")
    list_filter = ("status","priority","assigned_to")
    search_fields = ("title","customer","description")

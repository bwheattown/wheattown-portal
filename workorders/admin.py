from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import WorkOrder

@admin.register(WorkOrder)
class WorkOrderAdmin(admin.ModelAdmin):
    # keep the list view simple first
    list_display = ("id", "title", "status", "priority")
    # comment filters temporarily to rule out queryset issues
    # list_filter = ("status", "priority", "assigned_to")
    # search_fields = ("title", "customer", "description")
    # render FK with a lookup instead of loading all users
    raw_id_fields = ("assigned_to",)
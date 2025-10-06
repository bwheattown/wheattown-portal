from django.contrib import admin
from .models import WorkOrder

@admin.register(WorkOrder)
class WorkOrderAdmin(admin.ModelAdmin):
    # keep list simple
    list_display = ("id", "title", "status", "priority")

    # only expose safe fields on the create/edit form
    fields = ("title", "customer", "status", "priority", "description")

    # avoid rendering a heavy user dropdown (we're not showing it anyway)
    raw_id_fields = ("assigned_to",)

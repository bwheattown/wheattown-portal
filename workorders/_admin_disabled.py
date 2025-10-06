from django.contrib import admin

# Register your models here.

# workorders/admin.py
from django.contrib import admin
from .models import WorkOrder

@admin.register(WorkOrder)
class WorkOrderAdmin(admin.ModelAdmin):
<<<<<<< HEAD:workorders/admin.py
    pass
=======
    # keep the list view simple first
    list_display = ("id", "title", "status", "priority")
    # comment filters temporarily to rule out queryset issues
    # list_filter = ("status", "priority", "assigned_to")
    # search_fields = ("title", "customer", "description")
    # render FK with a lookup instead of loading all users
    raw_id_fields = ("assigned_to",)
>>>>>>> 94824a1bbcf74dfc56d614fcba99c46c884c2e11:workorders/_admin_disabled.py

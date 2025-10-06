#workorders/admin.py 

from django.contrib import admin
from .models import WorkOrder, Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "contact_name", "email", "phone")
    search_fields = ("name", "contact_name", "email", "phone")

@admin.register(WorkOrder)
class WorkOrderAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "customer", "status", "priority", "assigned_to", "due_date")
    list_filter = ("status", "priority", "assigned_to", "customer")
    search_fields = ("title", "description", "customer__name", "assigned_to__username")
    # Fast lookups (type-ahead) instead of giant dropdowns:
    autocomplete_fields = ("customer", "assigned_to")
    # Optional: keep form tidy
    fields = ("title","customer","status","priority","description","due_date","assigned_to","total_hours","total_cost")

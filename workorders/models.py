# workorders/models.py

from django.db import models
from django.contrib.auth import get_user_model

class WorkOrder(models.Model):
    class Status(models.TextChoices):
        OPEN = "OPEN", "Open"
        IN_PROGRESS = "IN_PROGRESS", "In Progress"
        HOLD = "HOLD", "On Hold"
        CLOSED = "CLOSED", "Closed"

    class Priority(models.IntegerChoices):
        LOW = 1, "Low"
        MEDIUM = 2, "Medium"
        HIGH = 3, "High"
        CRITICAL = 4, "Critical"

    title = models.CharField(max_length=200)
    customer = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.OPEN)
    priority = models.IntegerField(choices=Priority.choices, default=Priority.MEDIUM)
    description = models.TextField(blank=True)
    opened_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)
    assigned_to = models.ForeignKey(get_user_model(), null=True, blank=True, on_delete=models.SET_NULL)
    total_hours = models.DecimalField(max_digits=6, decimal_places=2, default=0, blank=True)   # <-- allow blank
    total_cost  = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True)  # <-- allow blank

    def __str__(self):
        return f"WO#{self.pk or '-'} · {self.title}"

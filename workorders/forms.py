#workorders/forms.py

from django import forms
from django.contrib.auth import get_user_model
from .models import WorkOrder, Customer

User = get_user_model()

class WorkOrderForm(forms.ModelForm):
    class Meta:
        model = WorkOrder
        fields = ["title","customer","status","priority","description","due_date","assigned_to","total_hours","total_cost"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["customer"].queryset = Customer.objects.order_by("name")
        self.fields["assigned_to"].queryset = User.objects.order_by("username")

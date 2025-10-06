#workorders/views.py

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import WorkOrder
from .forms import WorkOrderForm

@method_decorator(login_required, name="dispatch")
class WorkOrderList(ListView):
    model = WorkOrder
    paginate_by = 20
    ordering = ["-opened_at"]

@method_decorator(login_required, name="dispatch")
class WorkOrderDetail(DetailView):
    model = WorkOrder

@method_decorator(login_required, name="dispatch")
class WorkOrderCreate(CreateView):
    model = WorkOrder
    form_class = WorkOrderForm
    success_url = reverse_lazy("workorders:list")

@method_decorator(login_required, name="dispatch")
class WorkOrderUpdate(UpdateView):
    model = WorkOrder
    form_class = WorkOrderForm
    success_url = reverse_lazy("workorders:list")

@method_decorator(login_required, name="dispatch")
class WorkOrderDelete(DeleteView):
    model = WorkOrder
    success_url = reverse_lazy("workorders:list")


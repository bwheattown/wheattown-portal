#workorders/urls.py

from django.urls import path
from . import views

app_name = "workorders"

urlpatterns = [
    path("", views.WorkOrderList.as_view(), name="list"),
    path("new/", views.WorkOrderCreate.as_view(), name="create"),
    path("<int:pk>/", views.WorkOrderDetail.as_view(), name="detail"),
    path("<int:pk>/edit/", views.WorkOrderUpdate.as_view(), name="update"),
    path("<int:pk>/delete/", views.WorkOrderDelete.as_view(), name="delete"),
]

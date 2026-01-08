from django.urls import path
from .views import EmployeeCreateView

urlpatterns = [
    path('create/', EmployeeCreateView.as_view()),
]

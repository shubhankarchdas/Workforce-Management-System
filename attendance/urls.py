from django.urls import path
from .views import (
    AttendanceCreateView,
    AttendanceListView,
    AttendanceUpdateView,
    AttendanceDeleteView
)

urlpatterns = [
    path('create/', AttendanceCreateView.as_view()),
    path('list/', AttendanceListView.as_view()),
    path('update/<int:pk>/', AttendanceUpdateView.as_view()),
    path('delete/<int:pk>/', AttendanceDeleteView.as_view()),
]

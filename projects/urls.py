from django.urls import path
from .views import ProjectCreateView, ProjectListView

urlpatterns = [
    path('create/', ProjectCreateView.as_view()),
    path('list/', ProjectListView.as_view()),
]

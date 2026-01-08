from django.urls import path
from .views import OrganizationCreateView, OrganizationListView

urlpatterns = [
    path('create/', OrganizationCreateView.as_view()),
    path('list/', OrganizationListView.as_view()),
]

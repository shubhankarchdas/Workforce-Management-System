from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),

    path('api/org/', include('organizations.urls')),
    path('api/project/', include('projects.urls')),
    path('api/employee/', include('employees.urls')),
    path('api/attendance/', include('attendance.urls')),
    path('api/task/', include('tasks.urls')),
]

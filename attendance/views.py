from rest_framework.generics import (
    CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
)
from django.core.cache import cache
from .models import Attendance
from .serializers import AttendanceSerializer
from employees.permissions import IsOwnerOrManager
from rest_framework.permissions import IsAuthenticated


class AttendanceCreateView(CreateAPIView):
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrManager]

    def perform_create(self, serializer):
        attendance = serializer.save(created_by=self.request.user)
        cache_key = f"attendance_project_{attendance.project.id}"
        cache.delete(cache_key)   # 🔥 invalidate cache


class AttendanceListView(ListAPIView):
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        project_id = self.request.query_params.get('project')
        cache_key = f"attendance_project_{project_id}"

        cached_data = cache.get(cache_key)
        if cached_data:
            return cached_data

        queryset = Attendance.objects.filter(project_id=project_id)
        cache.set(cache_key, queryset, timeout=300)  # 5 minutes
        return queryset


class AttendanceUpdateView(UpdateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrManager]

    def perform_update(self, serializer):
        attendance = serializer.save()
        cache_key = f"attendance_project_{attendance.project.id}"
        cache.delete(cache_key)


class AttendanceDeleteView(DestroyAPIView):
    queryset = Attendance.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrManager]

    def perform_destroy(self, instance):
        cache_key = f"attendance_project_{instance.project.id}"
        cache.delete(cache_key)
        instance.delete()

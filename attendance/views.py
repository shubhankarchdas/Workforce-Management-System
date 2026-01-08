from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from .models import Attendance
from .serializers import AttendanceSerializer

class AttendanceCreateView(CreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class AttendanceListView(ListAPIView):
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        project_id = self.request.query_params.get('project')
        return Attendance.objects.filter(project_id=project_id)

class AttendanceUpdateView(UpdateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class AttendanceDeleteView(DestroyAPIView):
    queryset = Attendance.objects.all()

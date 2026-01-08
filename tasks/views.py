from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from .models import Task
from .serializers import TaskSerializer

class TaskCreateView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskListView(ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        project_id = self.request.query_params.get('project')
        return Task.objects.filter(project_id=project_id)

class TaskUpdateView(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

from employees.permissions import IsOwnerOrManager
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, ListAPIView
from .models import Project
from .serializers import ProjectSerializer

class ProjectCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated, IsOwnerOrManager]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectListView(ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        org_id = self.request.query_params.get('organization')
        return Project.objects.filter(organization_id=org_id)

from rest_framework.generics import CreateAPIView
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeCreateView(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

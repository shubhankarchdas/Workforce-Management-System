from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def validate(self, data):
        if not data['assigned_to'].projects.filter(id=data['project'].id).exists():
            raise serializers.ValidationError(
                "Employee is not assigned to this project"
            )
        return data

from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

    def validate(self, data):
        if data['organization'] is None:
            raise serializers.ValidationError("Employee must belong to organization")
        return data

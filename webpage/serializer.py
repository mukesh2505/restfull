from rest_framework import serializers
from .models  import Employee

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    # region=serializers.CharField(max_length=100,required=False)
    # description = serializers.CharField(max_length=400,required=False)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Employee
        fields = ('name','employee_id', 'desgination','owner')

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)


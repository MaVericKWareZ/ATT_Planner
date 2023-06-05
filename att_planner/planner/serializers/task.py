from rest_framework import serializers

from att_planner.planner.models.task import Task


class TaskWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('name', 'description', 'progress', 'priority', 'end_date', 'bucket', 'user')


class TaskReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'

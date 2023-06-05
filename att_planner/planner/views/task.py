from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser

from att_planner.planner.models import Task
from att_planner.planner.serializers.task import TaskWriteSerializer


class TaskViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    queryset = Task.objects.all()
    serializer_class = TaskWriteSerializer

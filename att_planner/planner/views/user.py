from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser

from att_planner.planner.models import User
from att_planner.planner.serializers.user import UserWriteSerializer


class UserViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    queryset = User.objects.all()
    serializer_class = UserWriteSerializer

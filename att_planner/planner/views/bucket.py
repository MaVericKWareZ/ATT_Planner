from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser

from att_planner.planner.models import Bucket
from att_planner.planner.serializers.bucket import BucketWriteSerializer


class BucketViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    queryset = Bucket.objects.all()
    serializer_class = BucketWriteSerializer

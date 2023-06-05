import logging

from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from att_planner.planner.models import Bucket, Task
from att_planner.planner.serializers.task import TaskReadSerializer

logger = logging.getLogger(__name__)


class BucketTasksView(ListAPIView):
    queryset = Task.objects.all()

    def get(self, request, *args, **kwargs):
        bucket_id = self.kwargs['id']
        logger.info(f'bucket tasks api called with bucket_id={bucket_id}')
        try:
            bucket = Bucket.objects.get(id=bucket_id)
            logger.info(f'retrieving tasks for bucket={bucket}')
            task_list = list(self.get_queryset().filter(bucket=bucket))
            task_serializer = TaskReadSerializer(task_list, many=True)
            tasks = task_serializer.data
            return Response(tasks, status=status.HTTP_200_OK)
        except Bucket.DoesNotExist:
            logger.error(f'bucket not found with bucket_id={bucket_id}')
            return Response({'error': 'bucket_id is invalid'}, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as e:
            error_message = e.detail
            logger.error(f'validation error with error_message={error_message}')
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)

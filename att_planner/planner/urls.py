from django.urls import path
from rest_framework.routers import SimpleRouter

from att_planner.planner.views.bucket import BucketViewSet
from att_planner.planner.views.bucket_tasks import BucketTasksView
from att_planner.planner.views.index import index
from att_planner.planner.views.task import TaskViewSet
from att_planner.planner.views.user import UserViewSet

router = SimpleRouter(trailing_slash=False)
router.register('tasks', TaskViewSet)
router.register('users', UserViewSet)
router.register('buckets', BucketViewSet)

urlpatterns = [path('', index, name='index'), path('buckets/<id>/tasks', BucketTasksView.as_view(), name='upload')]

urlpatterns += router.urls

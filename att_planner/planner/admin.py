from django.contrib import admin

from .models import Bucket, Task, User

admin.site.register(Task)
admin.site.register(User)
admin.site.register(Bucket)

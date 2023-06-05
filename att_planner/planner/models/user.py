from django.db import models

from att_planner.commons.models import CreatedModified


class User(CreatedModified):
    email_id = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self) -> str:
        return f'({self.id}: {self.user_name}, {self.email_id}, {self.is_active}, {self.last_login})'

    class Meta:
        db_table = 'user'
        app_label = 'planner'
        verbose_name = 'user'
        verbose_name_plural = 'users'

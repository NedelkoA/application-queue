from django.db import models

from accounts.models import User
from users.models import Application


class MyApplication(models.Model):
    operator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='work_app'
    )
    application = models.ForeignKey(
        Application,
        on_delete=models.SET_NULL,
        null=True,
        related_name='work_app'
    )

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


class ChangeLog(models.Model):
    operator = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='change_log'
    )
    application = models.ForeignKey(
        Application,
        on_delete=models.DO_NOTHING,
        related_name='change_log'
    )
    last_state = models.CharField(max_length=20)
    current_state = models.CharField(max_length=20)
    updated_on = models.DateTimeField(max_length=20)

    def __str__(self):
        return 'app_id: ' + str(self.application.pk) + ' date: ' + str(self.updated_on.date())

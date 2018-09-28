from django.db import models
from django.core.validators import RegexValidator

from accounts.models import User

CHOICES = [
    ('queue', 'Queue'),
    ('review', 'Under consideration'),
    ('work', 'In the work'),
    ('success', 'Successfully'),
    ('unsuccess', 'Unsuccessfully'),
]


class Application(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='application'
    )
    text = models.TextField()
    phone_number = models.CharField(
        max_length=13,
        validators=[
            RegexValidator('^\+380\d{9}$',
                           'Phone number must be entered in the format: \'+380xxxxxxxxx\'.')
        ]
    )
    email = models.EmailField(
        blank=True,
        null=True
    )
    status = models.CharField(
        max_length=20,
        choices=CHOICES,
        default='queue',
    )
    updated_on = models.DateTimeField(auto_now=True)

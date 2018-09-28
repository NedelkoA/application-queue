# Generated by Django 2.1.1 on 2018-09-28 06:02

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('phone_number', models.CharField(max_length=13, validators=[django.core.validators.RegexValidator('^\\+380\\d{9}$', "Phone number must be entered in the format: '+380xxxxxxxxx'.")])),
                ('email', models.EmailField(max_length=254)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='application', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

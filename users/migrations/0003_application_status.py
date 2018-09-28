# Generated by Django 2.1.1 on 2018-09-28 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180928_0608'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('queue', 'Queue'), ('review', 'Under consideration'), ('work', 'In the work'), ('success', 'Successfully'), ('unsuccess', 'Unsuccessfully')], default='queue', max_length=20),
        ),
    ]
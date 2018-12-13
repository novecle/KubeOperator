# Generated by Django 2.1.1 on 2018-11-02 09:14

import common.models
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CeleryTask',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('root_id', models.UUIDField()),
                ('name', models.CharField(max_length=1024)),
                ('state', models.CharField(choices=[('PENDING', 'Pending'), ('STARTED', 'Started'), ('SUCCESS', 'Success'), ('FAILURE', 'Failure'), ('RETRY', 'Retry')], default='PENDING', max_length=16)),
                ('result', common.models.JsonTextField(null=True)),
                ('date_start', models.DateTimeField(auto_now_add=True)),
                ('date_finished', models.DateTimeField(null=True)),
            ],
        ),
    ]

# Generated by Django 2.2.2 on 2019-06-24 20:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_auto_20190624_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='lists',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todolist.List'),
        ),
        migrations.AlterField(
            model_name='board',
            name='users',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='list',
            name='tasks',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todolist.Task'),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(null=True),
        ),
    ]

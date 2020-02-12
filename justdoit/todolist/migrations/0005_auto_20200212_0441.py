# Generated by Django 3.0 on 2020-02-12 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0004_auto_20200212_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='to_do',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', related_query_name='task', to='todolist.ToDo'),
        ),
    ]

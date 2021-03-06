# Generated by Django 3.0 on 2020-02-12 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_auto_20200212_0407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='tasks', related_query_name='task', to='todolist.Tag', verbose_name='Tags'),
        ),
    ]

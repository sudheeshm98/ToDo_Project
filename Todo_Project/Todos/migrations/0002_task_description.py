# Generated by Django 4.2.2 on 2023-07-03 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
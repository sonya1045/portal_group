# Generated by Django 5.1.3 on 2024-12-08 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_system', '0003_alter_homework_homework'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='homework',
            field=models.CharField(max_length=100),
        ),
    ]

# Generated by Django 4.1.4 on 2022-12-17 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_review', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]

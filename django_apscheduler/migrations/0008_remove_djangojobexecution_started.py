# Generated by Django 2.2.14 on 2020-07-20 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("django_apscheduler", "0007_auto_20200717_1404"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="djangojobexecution",
            name="started",
        ),
    ]

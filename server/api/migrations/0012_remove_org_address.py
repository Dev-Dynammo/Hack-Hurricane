# Generated by Django 5.0 on 2023-12-13 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_org_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='org',
            name='Address',
        ),
    ]

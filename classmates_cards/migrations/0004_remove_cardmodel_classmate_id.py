# Generated by Django 3.1.2 on 2021-01-09 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classmates_cards', '0003_auto_20210109_2340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardmodel',
            name='classmate_id',
        ),
    ]

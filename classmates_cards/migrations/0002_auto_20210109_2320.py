# Generated by Django 3.1.2 on 2021-01-09 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classmates_cards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('email', models.EmailField(max_length=254, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='GetCard',
        ),
    ]

# Generated by Django 3.2.15 on 2024-04-25 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='test',
            field=models.TextField(default=''),
        ),
    ]
# Generated by Django 4.1.7 on 2023-03-18 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_item_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='user_name',
        ),
    ]

# Generated by Django 3.0.3 on 2020-03-15 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_auto_20200314_0944'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='About',
            new_name='Stock',
        ),
    ]
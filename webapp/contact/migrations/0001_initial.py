# Generated by Django 3.0.3 on 2020-07-02 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('subject', models.TextField()),
                ('date', models.CharField(default='', max_length=12)),
                ('time', models.CharField(default='', max_length=12)),
                ('message', models.TextField()),
            ],
        ),
    ]

# Generated by Django 4.1.6 on 2023-03-27 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0012_signup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='contact',
            field=models.CharField(max_length=30),
        ),
    ]

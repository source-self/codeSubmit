# Generated by Django 2.2.5 on 2020-03-10 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coder', '0004_auto_20200310_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='time',
            field=models.DateTimeField(null=True),
        ),
    ]

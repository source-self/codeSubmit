# Generated by Django 2.2.5 on 2020-03-10 01:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coder', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vercode',
            old_name='content',
            new_name='code',
        ),
    ]

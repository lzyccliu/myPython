# Generated by Django 2.0 on 2017-12-12 01:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_auto_20171212_0930'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='brithday',
            new_name='birthday',
        ),
    ]

# Generated by Django 4.1.4 on 2022-12-20 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_alter_study_timestamp"),
    ]

    operations = [
        migrations.RenameField(
            model_name="study",
            old_name="timestamp",
            new_name="date",
        ),
    ]

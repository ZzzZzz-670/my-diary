# Generated by Django 5.2.3 on 2025-06-27 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0002_rename_pub_data_question_pub_date"),
    ]

    operations = [
        migrations.RenameField(
            model_name="choice",
            old_name="vores",
            new_name="votes",
        ),
    ]

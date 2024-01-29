# Generated by Django 4.2.8 on 2023-12-21 11:16

from django.db import migrations, models

import api.models.user


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0055_alter_longrunningjob_job_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="llm_settings",
            field=models.JSONField(default=api.models.user.get_default_llm_settings),
        ),
        migrations.AlterField(
            model_name="longrunningjob",
            name="job_type",
            field=models.PositiveIntegerField(
                choices=[
                    (1, "Scan Photos"),
                    (2, "Generate Event Albums"),
                    (3, "Regenerate Event Titles"),
                    (4, "Train Faces"),
                    (5, "Delete Missing Photos"),
                    (7, "Scan Faces"),
                    (6, "Calculate Clip Embeddings"),
                    (8, "Find Similar Faces"),
                    (9, "Download Selected Photos"),
                    (10, "Download Models"),
                ]
            ),
        ),
    ]
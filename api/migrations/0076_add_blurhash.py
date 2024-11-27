from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0075_alter_face_cluster_person"),
    ]
    operations = [
        migrations.AddField(
            model_name="Photo",
            name="blurhash",
            field=models.TextField(blank=True, null=True),
        ),
    ]

# Generated by Django 5.1.1 on 2024-09-11 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("comentarios", "0003_delete_topico"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pessoa",
            name="comentario",
            field=models.EmailField(max_length=500),
        ),
    ]

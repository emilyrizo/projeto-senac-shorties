# Generated by Django 5.1.1 on 2024-09-10 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("comentarios", "0002_topico"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Topico",
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-06 14:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Registro", "0002_alter_locales_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="locales",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]

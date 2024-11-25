# Generated by Django 5.0.3 on 2024-11-24 23:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("quotes", "0004_report"),
    ]

    operations = [
        migrations.AlterField(
            model_name="report",
            name="quote",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reports",
                to="quotes.quote",
            ),
        ),
    ]

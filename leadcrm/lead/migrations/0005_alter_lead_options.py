# Generated by Django 5.0.6 on 2024-07-01 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("lead", "0004_lead_team"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="lead",
            options={"ordering": ("name",)},
        ),
    ]
# Generated by Django 5.0.4 on 2024-05-22 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting_classifier_app', '0002_rename_town_or_village_voter_booth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='gender',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

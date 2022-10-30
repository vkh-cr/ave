# Generated by Django 4.1.2 on 2022-10-30 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("people", "0002_person_sections"),
        ("team", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="teamsection",
            name="members",
            field=models.ManyToManyField(
                through="team.TeamMembership", to="people.person"
            ),
        ),
    ]
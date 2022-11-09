# Generated by Django 4.1.2 on 2022-11-09 19:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False)),
                ("code", models.CharField(blank=True, max_length=3)),
                ("name", models.CharField(max_length=256)),
                ("e_mail", models.EmailField(blank=True, max_length=128)),
                ("phone", models.CharField(blank=True, max_length=128)),
                ("city", models.CharField(blank=True, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name="TeamMembership",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False)),
                (
                    "person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="member_sections",
                        to="people.person",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TeamSection",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False)),
                ("code", models.CharField(max_length=32)),
                ("name", models.CharField(max_length=256)),
                ("e_mail", models.EmailField(blank=True, max_length=128)),
                ("phone", models.CharField(blank=True, max_length=128)),
                (
                    "members",
                    models.ManyToManyField(
                        through="people.TeamMembership", to="people.person"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="teammembership",
            name="section",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.RESTRICT,
                related_name="member_persons",
                to="people.teamsection",
            ),
        ),
        migrations.AddField(
            model_name="person",
            name="sections",
            field=models.ManyToManyField(
                through="people.TeamMembership", to="people.teamsection"
            ),
        ),
        migrations.AddConstraint(
            model_name="teamsection",
            constraint=models.UniqueConstraint(
                models.F("code"), name="uniq_section_code"
            ),
        ),
        migrations.AddConstraint(
            model_name="teammembership",
            constraint=models.UniqueConstraint(
                models.F("person"), models.F("section"), name="uniq_team_membership"
            ),
        ),
        migrations.AddConstraint(
            model_name="person",
            constraint=models.UniqueConstraint(
                models.F("code"), name="uniq_person_code"
            ),
        ),
    ]
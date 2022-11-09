from . import models

from django.contrib import admin


@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "uuid",
    )


@admin.register(models.TeamSection)
class TeamSectionAdmin(admin.ModelAdmin):
    list_display = (
        "code",
        "name",
        "uuid",
    )


@admin.register(models.TeamMembership)
class TeamMembership(admin.ModelAdmin):
    list_display = (
        "__str__",
        "person",
        "section",
    )

    list_filter = ("section",)

    raw_id_fields = (
        "person",
        "section",
    )

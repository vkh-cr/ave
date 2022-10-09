from . import models

from django.contrib import admin


@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "uuid",
    )

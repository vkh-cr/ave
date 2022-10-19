from wagtail import hooks
from wagtail.admin.panels import InlinePanel
from wagtail.admin.search import SearchArea
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
    ModelAdminGroup,
)

from people.models import Person
from team.models import TeamSection


class TeamSectionAdmin(ModelAdmin):
    model = TeamSection
    base_url_path = "team/sections"
    # menu_label = "Sections"
    menu_icon = "user"
    menu_order = 300
    # or True to add your model to the Settings sub-menu
    add_to_settings_menu = False
    # or True to exclude pages of this type from Wagtail's explorer view
    exclude_from_explorer = False
    # or False to exclude your model from the menu
    add_to_admin_menu = True
    list_display = ("name", "e_mail")
    # list_filter = ("author",)
    search_fields = ("name", "e_mail")
    ordering = ("name",)
    inspect_view_enabled = True


class PersonAdmin(ModelAdmin):
    model = Person
    base_url_path = "team/persons"
    # menu_label = "Persons"
    menu_icon = "user"
    menu_order = 200
    # or True to add your model to the Settings sub-menu
    add_to_settings_menu = False
    # or True to exclude pages of this type from Wagtail's explorer view
    exclude_from_explorer = False
    # or False to exclude your model from the menu
    add_to_admin_menu = True
    list_display = ("name", "code", "e_mail", "phone", "city")
    search_fields = ("name", "e_mail", "city")
    ordering = ("name",)
    inspect_view_enabled = True


class TeamGroup(ModelAdminGroup):
    menu_label = "Team"
    menu_icon = "group"  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (
        PersonAdmin,
        TeamSectionAdmin,
    )


modeladmin_register(TeamGroup)


@hooks.register("register_admin_search_area")
def register_persons_search_area():
    index_url = PersonAdmin().url_helper.index_url

    return SearchArea(
        "Persons",
        index_url,
        icon_name="user",
        order=10000,
    )


@hooks.register("register_admin_search_area")
def register_sections_search_area():
    index_url = TeamSectionAdmin().url_helper.index_url

    return SearchArea(
        "Team sections",
        index_url,
        icon_name="group",
        order=10001,
    )

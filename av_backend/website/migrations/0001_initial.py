# Generated by Django 4.1.2 on 2022-11-09 19:28

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
import website.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailcore", "0077_alter_revision_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="HomePage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "body",
                    wagtail.fields.StreamField(
                        [
                            (
                                "paragraph",
                                wagtail.blocks.RichTextBlock(
                                    features=[
                                        "h2",
                                        "h3",
                                        "h4",
                                        "bold",
                                        "italic",
                                        "superscript",
                                        "subscript",
                                        "strikethrough",
                                        "ol",
                                        "ul",
                                        "hr",
                                        "link",
                                        "document-link",
                                    ]
                                ),
                            ),
                            ("image", wagtail.images.blocks.ImageChooserBlock()),
                            (
                                "person",
                                wagtail.blocks.StructBlock(
                                    [
                                        ("first_name", wagtail.blocks.CharBlock()),
                                        ("surname", wagtail.blocks.CharBlock()),
                                        (
                                            "photo",
                                            website.blocks.ImageChooserBlock(
                                                required=False
                                            ),
                                        ),
                                        ("biography", wagtail.blocks.RichTextBlock()),
                                    ]
                                ),
                            ),
                        ],
                        blank=True,
                        use_json_field=True,
                        verbose_name="body",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
    ]
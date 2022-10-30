from django.db import models as m
from django.utils.translation import gettext_lazy as _
from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock

from wagtail.models import Page

from home.blocks import RICH_TEXT_BLOCK_FEATURES


class CommonBlocks(blocks.StreamBlock):
    paragraph = blocks.RichTextBlock(features=RICH_TEXT_BLOCK_FEATURES)
    image = ImageChooserBlock()


class HomePage(Page):
    body = StreamField(
        CommonBlocks(),
        use_json_field=True,
        blank=True,
        verbose_name=_("body"),
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]

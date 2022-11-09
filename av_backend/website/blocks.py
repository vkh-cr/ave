from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock as OrigImageChooserBlock

RICH_TEXT_BLOCK_FEATURES = [
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


class ImageChooserBlock(OrigImageChooserBlock):
    ...


class PersonBlock(blocks.StructBlock):
    first_name = blocks.CharBlock()
    surname = blocks.CharBlock()
    photo = ImageChooserBlock(required=False)
    biography = blocks.RichTextBlock()

    class Meta:
        template = "home/blocks/person.html"
        icon = "user"

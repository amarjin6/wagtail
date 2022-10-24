from django.db import models

from wagtail.models import Page
from wagtail.core.fields import StreamField, StreamBlock
from wagtail.core.blocks import RichTextBlock, CharBlock, StructBlock, TextBlock, ChoiceBlock, PageChooserBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.embeds.blocks import EmbedBlock
from home.enums import Size


class HomePage(Page):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    hero_text = models.CharField(
        max_length=100,
        help_text='Write an introduction for the bakery',
        null=True,
    )

    hero_CTA = models.CharField(
        max_length=100,
        help_text='Text to display on Call to Action',
        null=True,
    )

    section_2 = StreamField([
        ('home_content_block', StreamBlock([
            ('heading_block', StructBlock([
                ('heading_text', CharBlock(
                    required=True,
                )),
                ('size', ChoiceBlock(
                    required=False,
                    choices=Size.choices(),
                    default=Size.DEFAULT.name,
                ))
            ],
                icon='title',
            )),
            ('paragraph_block', RichTextBlock(
                icon='',
            )),
            ('image_block', StructBlock([
                ('image', ImageChooserBlock(
                    required=True,
                )),
                ('caption', CharBlock(
                    required=False,
                )),
                ('attribution', CharBlock(
                    required=False,
                ))
            ],
                icon='image',
            )),
            ('block_quote', StructBlock([
                ('text', TextBlock(
                    required=True,
                )),
                ('author', CharBlock(
                    required=False,
                    label='e.g. Mary Berry',
                ))
            ],
                icon='',

            )),
            ('embed_block', EmbedBlock(
                help_text='Insert an embed URL e.g. https://www.youtube.com/watch?v=SGJFWirQ3ks',
                icon='',
            )),

        ],
            icon='arrow-down-big',
        )),
    ], blank=True, use_json_field=True)

    section_3 = StreamField([
        ('section_3', StructBlock([
            ('featured_section_1_title', CharBlock(
                required=False,
                help_text='Title to display above the promo copy',
                icon='',
            )),
            ('featured_section_1', PageChooserBlock(
                help_text='First featured section for the homepage. Will display up to three child items.',
                required=False,
            )),
            ('featured_section_2_title', CharBlock(
                required=False,
                help_text='Title to display above the promo copy',
                icon='',
            )),
            ('featured_section_2', PageChooserBlock(
                help_text='Second featured section for the homepage. Will display up to three child items.',
                required=False,
            )),
            ('featured_section_3_title', CharBlock(
                required=False,
                help_text='Title to display above the promo copy',
                icon='',
            )),
            ('featured_section_3', PageChooserBlock(
                help_text='Third featured section for the homepage. Will display up to six child items.',
                required=False,
            )),
        ], icon='arrow-down-big')),
    ], blank=True, use_json_field=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('image'),
            FieldPanel('hero_text'),
            FieldPanel('hero_CTA'),
        ], heading='Section 1'),
        FieldPanel('section_2'),
        FieldPanel('section_3'),
    ]

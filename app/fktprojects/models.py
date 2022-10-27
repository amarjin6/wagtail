from django.db import models
from django.core.validators import RegexValidator
from datetime import datetime

from wagtail.models import Page
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.blocks import CharBlock, PageChooserBlock
from wagtail_color_panel.fields import ColorField
from wagtail_color_panel.edit_handlers import NativeColorPanel

from core.enums import Gender, Role, Status, Palette


class FKTPage(Page):
    subpage_types = [
        'fktprojects.ProjectPage',
    ]


class ProjectPage(Page):
    # Section user
    gender = models.CharField(
        max_length=15,
        choices=Gender.choices(),
        default=Gender.DEFAULT.name,
        null=True,
    )

    phone_regex = RegexValidator(regex=r'^\+?1?\d{12,12}$',
                                 message="Phone number must be entered in the format: '+XXX-XX-XXX-XX-XX',"
                                         " e.g. +375291234567.")

    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=12,
        null=True,
        blank=False,
    )

    founder = models.CharField(
        max_length=64,
        null=True,
    )

    foundation_date = models.DateField(
        null=True,
    )

    acronym = models.CharField(
        max_length=10,
        null=True
    )

    requested_role = models.CharField(
        max_length=9,
        choices=Role.choices(),
        default=Role.DEFAULT.name,
        null=True,
    )

    first_name = models.CharField(
        max_length=64,
        null=True,
    )

    last_name = models.CharField(
        max_length=64,
        null=True,
    )

    username = models.CharField(
        max_length=32,
        unique=True,
        null=True,
    )

    email = models.EmailField(
        unique=True,
        null=True,
    )

    # Section project
    status = models.CharField(
        max_length=10,
        choices=Status.choices(),
        default=Status.DEFAULT.name,
        null=True,
    )

    COLOR_PALETTE = [
        ("#FF0000", "red",),
        ("#0000FF", "blue",),
        ("#00FF00", "green",),
        ("#000000", "black",),
        ("#808080", "grey",),
    ]

    marker = ColorField(
        choices=Palette.choices(),
        default=Palette.RED.value,
        null=True,
    )

    now = datetime.now()
    time = now.strftime("%d/%m/%Y %H:%M:%S")
    info = models.CharField(
        default='user ' + 'user' + ' created at ' + time,
        null=True,
        max_length=50,
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('gender'),
                FieldPanel('phone_number'),
                MultiFieldPanel(
                    [
                        FieldPanel('founder'),
                        FieldPanel('foundation_date'),
                        FieldPanel('acronym'),
                    ],
                    heading='University'
                ),
                FieldPanel('requested_role'),
                FieldPanel('first_name'),
                FieldPanel('last_name'),
                FieldPanel('username'),
                FieldPanel('email'),
            ],
            heading='User'
        ),

        MultiFieldPanel(
            [
                FieldPanel('status'),
                NativeColorPanel('marker'),
                FieldPanel('info'),
            ],
            heading='Project'
        )
    ]

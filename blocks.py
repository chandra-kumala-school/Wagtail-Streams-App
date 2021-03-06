from wagtail.admin.edit_handlers import (
    FieldPanel,
)
from wagtail.core.blocks import (
    URLBlock, 
    TextBlock, 
    ListBlock,
    CharBlock, 
    StreamBlock, 
    StructBlock, 
    BooleanBlock,
    RichTextBlock, 
)
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.blocks.field_block import PageChooserBlock

from wagtailcodeblock.blocks import CodeBlock

class ContentStreamBlock(StreamBlock):
    heading = TextBlock()
    paragraph = TextBlock()
    code = CodeBlock(label='Code')

    class Meta:
        icon='code'

class QuoteBlock(StructBlock):
    quotation = TextBlock(required=True, max_length=400)
    leadtext = CharBlock(required=False, max_length=50)
    source = CharBlock(required=True, max_length=50)


class CardBlock(StructBlock):
    # Single Horizontal Card
    image = ImageChooserBlock(required=True)
    title = CharBlock(required=True, max_length=40)
    text = TextBlock(required=True, max_length=200)
    button_page = PageChooserBlock(required=False)
    button_url = URLBlock(required=False, help_text='If nothing selected above.')

    class Meta:
        template = 'streams/card_block.html'
        icon = 'placeholder'
        label = 'Add single full width card'


class CardGroupBlock(StructBlock):
    # Multiple Vertical Cards
    title = CharBlock(required=False, help_text="Add title ...")

    cards = ListBlock(CardBlock)
    
    class Meta:
        template = 'streams/card_group_block.html'
        icon = 'placeholder'
        label = 'Add multiple cards'


class ButtonBlock(StructBlock):
    text = CharBlock(blank=True)
    classes = CharBlock(blank=True)
    link = URLBlock(required=False, label="external URL", blank=True)
    pagelink = PageChooserBlock(required=False, label="internal URL", blank=True)

    class Meta:
        template = "streams/button_block.html"
        icon = 'form'
        label = 'Individual button'

class ButtonGroupBlock(StructBlock):
    title = CharBlock(required=False, help_text="Add title ...")

    buttons = ListBlock(ButtonBlock)

    class Meta:
        template = "streams/button_group_block.html"
        icon = 'form'
        label = 'Button group'


class RichTextBlock(RichTextBlock):
    class Meta:
        template = 'streams/richtext_block.html'
        icon = 'doc-full'
        label = 'Full RichText'

class SimpleTextBlock(RichTextBlock):
    def __init__(self, required=True, help_text=None, editor='default', features=None, **kwargs):
        super().__init__(**kwargs)
        self.features = [
            "bold",
            "italic",
            "link",
        ]

    class Meta:
        template = 'streams/richtext_block.html'
        icon = 'doc-full'
        label = 'Full RichText'

class TestimonialBlock(StructBlock):
    test_name = TextBlock(blank=True)
    test_quote = TextBlock(blank=True)
    test_pic = ImageChooserBlock(blank=True)
    test_reversed = BooleanBlock(required=False, default=False)

    panels = [
        FieldPanel('intro')
    ]

    class Meta:
        template = "streams/testimonial_block.html"
        icon = 'group'
        label = 'Client Testimonial'

class SlideBlock(StructBlock):
    title = CharBlock("Title ...", blank=True, max_length=250)
    classesTitle = CharBlock(label="Title CSS (text-dark etc)", required=False, blank=True)
    caption = TextBlock(required=False, blank=True)
    classesCaption = CharBlock(label="Caption CSS (text-danger)", required=False, blank=True)
    classes = CharBlock(label="CSS classes (bg-light or bg-dark)", required=False, blank=True)
    background = ImageChooserBlock()
    button = TextBlock(required=False)
    link = URLBlock(required=False)


class CarouselBlock(StructBlock):
    slides = ListBlock(SlideBlock)
 
    class Meta:
        template = "streams/carousel_block.html"
        icon = 'image'
        label = 'Carousel'

class HeroBlock(StructBlock):
    heading = CharBlock(classname="full title", blank=True)
    classesHeading = CharBlock(label="Heading CSS (text-dark etc)", required=False, blank=True)
    text = TextBlock(required=False, blank=True)
    classesText = CharBlock(label="CSS classes for Text (text-success etc)", required=False, blank=True)
    classes = CharBlock(label="CSS classes from BS (bg-light or bg-dark)", required=False, blank=True)
    background = ImageChooserBlock(required=False, blank=True)
    buttonLabel = CharBlock(required=False, label="Text on button", blank=True)
    buttonUrl = URLBlock(required=False, blank=True)
 
    class Meta:
        template = "streams/jumbotron_block.html"
        icon = 'image'
        label = 'Hero / Jumbotron'


class CommonStreamBlock(StreamBlock):
    # Simple Blocks
    title = CharBlock(classname="full title", blank=True, max_length=200, icon='title', template='streams/title_block.html')
    videoembed = EmbedBlock("Video embed (YouTube and Facebook)", label='Enter Video URL',  max_length=500, icon='media', null=True, blank=True, template='streams/video_embed_block.html')
    image = ImageChooserBlock("Choose an image ...", label='Choose an image ...', icon='image', template='streams/image_block.html')
    googlemap = CharBlock("Google Calendar URL", label='Enter Google Map URL', icon='site', max_length=500, null=True, blank=True, template='streams/google_map_block.html')
    googlecal = CharBlock("Google Calendar URL", label='Enter Google Calendar URL', max_length=500, icon='date', null=True, blank=True, template='streams/google_cal_block.html')
    # Complex Blocks
    code = ContentStreamBlock()
    hero = HeroBlock()
    richtext = RichTextBlock()
    card = CardBlock()
    cards = CardGroupBlock()
    carousel = CarouselBlock()
    button = ButtonBlock()
    buttongroup = ButtonGroupBlock()
    testimonial = TestimonialBlock()

    class Meta:
        icon = 'cogs'
        null = True
        blank = True
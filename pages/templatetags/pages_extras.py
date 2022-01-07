from django import template
from pages.models import Page

# Registrar este template propio a la libreria de templates

register = template.Library()

@register.simple_tag

# base.html-footer
def get_page_list():
    pages = Page.objects.all()
    return pages
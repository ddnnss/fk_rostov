
from django import template

from pytils.translit import slugify

register = template.Library()


@register.filter
def get_sector(data):

    return f'<g data-sector={data["sector"]} class="sector-item" @click="sectorInfo($event)">{data["draw"]}</g>'


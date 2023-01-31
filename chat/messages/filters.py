from django.template.defaulttags import register
from datetime import datetime, date


@register.filter
def format_date(value) -> str:
    if isinstance(value, datetime):
        return value.strftime('%Y.%m.%d %H:%M')
    if isinstance(value, date):
        return value.strftime('%Y.%m.%d')
    return value

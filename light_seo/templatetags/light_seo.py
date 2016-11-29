# coding=utf-8;

__all__ = ['seo_title', 'seo_description', 'seo_keywords']
__author__ = 'Sergey Khaylov'
__email__ = 'Sergey.Haylov@gmail.com'


from django import template
from django.conf import settings
from django.utils.safestring import mark_safe


register = template.Library()


@register.simple_tag(takes_context=True)
def seo_title(context, **kwargs):
    kwargs = kwargs or {}
    kwargs['SEO_TITLE'] = context.get('SEO_TITLE', '')
    title = settings.SEO_TITLE_PATTERN.format(**kwargs)
    return mark_safe(u'<title>{}</title>'.format(title))


@register.simple_tag(takes_context=True)
def seo_description(context, **kwargs):
    kwargs = kwargs or {}
    description = context.get('SEO_DESCRIPTION', '') or ''
    description = u' '.join(description.split('\n'))
    return mark_safe(
        u'<meta name="description" content="{}">'.format(description)
    )


@register.simple_tag(takes_context=True)
def seo_keywords(context, **kwargs):
    kwargs = kwargs or {}
    keywords = context.get('SEO_KEYWORDS', '') or ''
    keywords = ','.join([k.strip() for k in keywords.split(',') if k.strip()])
    keywords = keywords.replace('\n', ' ')
    return mark_safe(u'<meta name="keywords" content="{}">'.format(keywords))

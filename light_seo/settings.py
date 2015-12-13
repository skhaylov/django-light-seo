# coding=utf-8;

__author__ = 'Sergey Khaylov'
__email__ = 'Sergey.Haylov@gmail.com'


from django.conf import settings

SEO_TITLE_PATTERN = getattr(settings, 'SEO_TITLE_PATTERN', u'{SEO_TITLE}')

# coding=utf-8;

__all__ = ['SEOModel']
__author__ = 'Sergey Khaylov'
__email__ = 'Sergey.Haylov@gmail.com'


from django.db import models
from django.utils.translation import gettext as _


class SEOModel(models.Model):
    seo_description = models.TextField(
        _('SEO description'), null=True, blank=True, default=None)
    seo_keywords = models.TextField(
        _('SEO keywords'), null=True, blank=True, default=None)

    class Meta:
        abstract = True

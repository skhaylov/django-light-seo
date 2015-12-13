# coding=utf-8;

__all__ = ['SEOViewMixin']
__author__ = 'Sergey Khaylov'
__email__ = 'Sergey.Haylov@gmail.com'


class SEOViewMixin(object):
    seo_title = None

    def get_seo_title(self):
        # Can be override
        return self.seo_title

    def get_seo_description(self):
        return self.object.seo_description

    def get_seo_keywords(self):
        return self.object.seo_keywords

    def get_context_data(self, **kwargs):
        def set_seo_attr(key, method=None):
            default_method = lambda: ''
            method = method or default_method
            try:
                value = method()
            except AttributeError:
                value = default_method()
            context[key] = value

        context = super(SEOViewMixin, self).get_context_data(**kwargs)

        set_seo_attr('SEO_TITLE', self.get_seo_title)
        set_seo_attr('SEO_DESCRIPTION', self.get_seo_description)
        set_seo_attr('SEO_KEYWORDS', self.get_seo_keywords)

        return context

from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Product
from django.urls import reverse
from django.utils.feedgenerator import Atom1Feed
from django.utils.text import slugify
from django.utils.html import strip_tags, escape, conditional_escape, format_html
from .templatetags.tags import unes_ht
import html

 
class ProductFeed(Feed):
    title = "kikabu"
    link = ""
    description = "feed of kikabu.com.ng"
 
    def items(self):
        return Product.objects.filter(status='Published')
 
    def item_title(self, item):
        return item.name
       
    def item_description(self, item):
        text = unes_ht(item.description)
        return truncatewords(text, 130)
 
    def item_link(self, item):
        na = slugify(item.name, allow_unicode=True)
        return reverse('post-detail', kwargs={'name': na, 'pk': item.pk})

        
    def item_file(self, item):
        domain = 'https://kikabu.com.ng'
        return item.file.url
 
 
class atomFeed(Feed):
    feed_type = Atom1Feed
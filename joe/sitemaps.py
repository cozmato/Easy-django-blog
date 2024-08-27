from django.contrib.sitemaps import Sitemap
from .models import Product


class ProductSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = 'https'
    
    def items(self):
        return Product.objects.filter(status='Published')




        
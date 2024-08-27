from django.urls import path, register_converter
from . import views
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from .utils import HashIdConverter
from django.contrib.sitemaps.views import sitemap
from .sitemaps import ProductSitemap
from django.views.generic.base import TemplateView
from .feeds import ProductFeed

register_converter(HashIdConverter, "hashid")

sitemaps = {
    'product': ProductSitemap,
}

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path("feed", ProductFeed(), name="feed"),
    path("ads.txt",TemplateView.as_view(template_name="Ads.txt", content_type="text/plain")),
    path("robots.txt",TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('searchfilter', views.searchfilter, name='search-filter'),
    path('', views.post_list, name='home'),
    path('about', views.about, name="about"),
    path('gdpr-policy', views.gdpr, name="gdpr-policy"),
    path('contact-us', views.contactus, name="contact_us"),
    path('privacy-policy', views.privacy_policy, name="privacy_policy"),
    path('disclaimer', views.disclaimer, name="disclaimer"), 
    path('termsandcondition', views.terms_condition, name="terms_condition"),
    path('search', views.search, name='search'),
    path('ajaxsearch', views.ajaxsearch, name='ajaxsearch'),
    path('<name>/<hashid:pk>/', views.post_detail, name='post-detail'),
    path('bassdxzd/', views.base, name='basssssszz'),
    path('category/<name>/<id>', views.cati, name='category'),

]

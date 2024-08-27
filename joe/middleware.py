import datetime
from django.core.cache import cache
from django.conf import settings

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object


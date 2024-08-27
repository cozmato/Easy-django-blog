from django.db.models.signals import post_save
# from django.contrib.auth.models import User
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.signals import user_logged_in, user_logged_out




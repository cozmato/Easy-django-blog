import datetime
from django.core.cache import cache
from django.db import models
from django.contrib.auth.models import User, AbstractUser, BaseUserManager
from django.urls import reverse
from PIL import Image, ImageOps
import PIL
from django.conf import settings
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from datetime import timedelta
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage, send_mail, EmailMultiAlternatives
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.db import models
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.text import slugify
from .utils import h_encode
from ckeditor_uploader.fields import RichTextUploadingField


def user_directory_path_profile(instance, filename):
    return 'user_{0}/profile.png'.format(instance.user.username)


class User(AbstractUser):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    username = models.CharField(unique=True, max_length=30)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ["first_name", "last_name", "username"]


class EmailMsg(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.CharField(max_length=300)
    date = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name



class ViewCount(models.Model):
    ip = models.CharField(max_length=50)
    click_from = models.CharField(max_length=500, default='', blank=True, null=True)
    session = models.CharField(max_length=100, default='', blank=True, null=True)
    state = models.CharField(max_length=100, default='', blank=True, null=True)
    country = models.CharField(max_length=100, default='', blank=True, null=True)



class Category(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=100)
    
    class Meta:
        indexes = [models.Index(fields=['image', 'name'])]

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return  f'/category/{self.name}'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 200 or img.width > 200:
            img.thumbnail((200, 200))
            
            original = ImageOps.exif_transpose(img)
            stripped = Image.new(original.mode, original.size)
            stripped.putdata(list(original.getdata()))
            stripped.save(self.image.path)



class Product(models.Model):
    STATUS = (
    ('Draft', 'Draft'),
    ('Published', 'Published'),
    )

    CURRENCY = (
        ('$', '$'),
        ('₦', '₦'),
        ('£', '£'),
        ('€', '€'),
        ('₣', '₣'),
        ('¥', '¥'),
        ('৳', '৳'),
        ('лв', 'лв'),
        ('L', 'L'),
        ('Bs.', 'Bs.'),
        ('R$', 'R$'),
        ('Kč', 'Kč'),
        ('₵', '₵'),
        ('₪', '₪'),
        ('₩', '₩'),
        ('〒', '〒'),
        ('zł', 'zł'),
        ('฿', '฿'),
        ('T$', 'T$'),
        ('₴', '₴'),
        ('₫', '₫'),
        ('R', 'R'),
        ('ZK', 'ZK'),
        ('Sh', 'Sh'),
        ('B/.', 'B/.'),
    )
    

    file = models.FileField(upload_to="product_pic", blank=True, null=True)
    name = models.CharField(max_length=200)
    Affiliate_link = models.URLField(blank=True, help_text='this field is optional')
    meta_description = models.CharField(max_length=200)
    content = RichTextUploadingField(default=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category", blank=True, null=True, default=None)
    status = models.CharField(max_length=11, choices=STATUS, default='Published')
    date = models.DateTimeField(auto_now_add=True)
    views = models.ManyToManyField(ViewCount, related_name="views")

    class Meta:
        ordering = ['-date']
        indexes = [models.Index(fields=['name', 'status', 'Affiliate_link', 'meta_description', 'category', 
                  'content'])]


    def total_views(self):
        return self.views.count()


    def get_hashid(self):
        return h_encode(self.id)
        

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        value = self.name
        na = slugify(value, allow_unicode=True)
        return reverse('post-detail', kwargs={'name': na, 'pk': self.pk}) 
        
    def save(self, force_insert=False, force_update=False, using=None,
         update_fields=None):
        super().save()

        p = f'{self.file.path}'
        if 'jpg' in p or 'gif' in p or 'jpng' in p or 'png' in p:
            img = Image.open(self.file.path)
            if img.height > 350 or img.width > 350:
                img.thumbnail((350, 350)) 
                
                original = ImageOps.exif_transpose(img)
                stripped = Image.new(original.mode, original.size)
                stripped.putdata(list(original.getdata()))
                stripped.save(self.file.path)



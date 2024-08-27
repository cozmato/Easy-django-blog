from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string, get_template
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.db.models import Q
from .models import *
from django.db.models import Max, Min, Sum, Subquery, OuterRef, Count
from django.core.exceptions import ValidationError
import sys
import os
import re
from django.template import Context
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, Page
from django.http import HttpResponseRedirect, JsonResponse
from .models import *
from django.http.response import JsonResponse
from datetime import timedelta
UserModel = get_user_model()
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View

import datetime
from datetime import date
import uuid
import html
from django.utils.html import strip_tags, escape, conditional_escape, format_html
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordResetForm
from django.views.decorators.cache import cache_page
from django.utils.text import slugify
from .templatetags.tags import conv, unes_ht
from .utils import get_ip, h_encode
from django.utils.text import slugify


# def error_404(request, exception):
#     data = {}
#     return render(request, '404.html', data)


def error_403(request, exception):
    data = {}
    return render(request, '403.html', data)
    
    
def error_500(request):
    data = {}
    return render(request, '500.html', data)



def about(request):

    return render(request, 'about.html')


def contactus(request):

    return render(request, 'contact_us.html')


def gdpr(request):

    return render(request, 'gdpr.html')
    

def terms_condition(request):

    return render(request, 'Terms and Condition.html')


def base(request):

    return render(request, 'base.html')


def privacy_policy(request):

    return render(request, 'privacy.html')


def disclaimer(request):

    return render(request, 'disclaimer.html')


def cati(request, name, id):
    cat = Category.objects.get(id=id)
    ca = Product.objects.filter(category=cat, status='Published')

    page = request.GET.get('page',1)
    paginator = Paginator(ca, 3)
    try:
        users_paginator = paginator.get_page(page)
    except PageNotAnInteger:
        users_paginator = paginator.page(1)
    except EmptyPage:
        users_paginator = paginator.page(paginator.num_pages)


    con = {
        'cat': cat,
        'ca': ca,
        'users': users_paginator,
    }

    return render(request, 'category.html', con)
   


def post_list(request):
    product = Product.objects.filter(status='Published').order_by('-id')
    ca = Category.objects.order_by('-id')

    pa = request.GET.get('page',1)
    paginate = Paginator(product, 3) 
    try:
        users_pag = paginate.get_page(pa)
    except PageNotAnInteger:
        users_pag = paginate.page(1)
    except EmptyPage:
        users_pag = paginate.page(paginate.num_pages)


    context = {
        'category': ca,
        'users_pag': users_pag,
    }
    return render(request, 'post_list.html', context)



def post_detail(request, name, pk):

    copo = get_object_or_404(Product, pk=pk)
    
    da = datetime.date.today()
    post = Product.objects.get(pk=pk, name=copo.name)
    
    
    click_from = request.META.get('HTTP_REFERER')

    ip = get_ip(request)
    device = uuid.UUID(int=uuid.getnode())
   
    if ViewCount.objects.filter(ip=ip).exists():
        post.views.add(ViewCount.objects.get(ip=ip))

    else:
        ViewCount.objects.create(ip=ip, click_from=click_from)
        post.views.add(ViewCount.objects.get(ip=ip, click_from=click_from))

   
    similar = Product.objects.filter(status='Published', category=post.category).exclude(id=post.id)[:4]
   
    context = {
        'da': da,
        'similar': similar,
        'total_views': post.total_views(),
        'post': post,
    }


    return render(request, 'post_detail.html', context)


def base(request):
    se = Product.objects.all()

    return {
        'se': se,
        }


def search(request):
    query = request.GET.get('q')
    se = ""
    if query:
        se = Product.objects.filter(name__icontains=query, status='Published')

    context = {
        'se': se,
    }
    return render(request, 'search.html', context)


def searchfilter(request):
    query = request.POST.get('q')
    se = ""
    if query:
        se = Product.objects.filter(name__icontains=query, status='Published')

    context = {
        'se': se,
    }
    t=render_to_string('search-filter.html', context)
    return JsonResponse({'data':t})


def ajaxsearch(request):
    query = request.POST.get('q')

    se = Product.objects.filter(name__icontains=query, status='Published')

    context = {
        'se': se[:10],
    }
    t=render_to_string('se-fi.html', context)
    return JsonResponse({'data':t})
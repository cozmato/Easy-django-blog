from django.db.models import FileField
from django.forms import forms
from django.template.defaultfilters import filesizeformat

from jinjo.settings import CONTENT_TYPES, MAX_UPLOAD_SIZE


def clean_file(value):
    content_type = value.content_type.split('/')[0]
    if content_type in CONTENT_TYPES:
        if value.size > int(MAX_UPLOAD_SIZE):
            raise forms.ValidationError('please keep filesize under %s. Current filesize is %s') % (
            filesizeformat(MAX_UPLOAD_SIZE), filesizeformat(value.size))
    else:
        raise forms.ValidationError('Filetype not supported')
    return value
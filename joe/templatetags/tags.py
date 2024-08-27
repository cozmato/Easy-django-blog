from django import template,templatetags
from django.contrib.auth.models import User
#from translate import Translator
#from deep_translator import GoogleTranslator
from decimal import Decimal
import datetime
from django.utils.text import slugify
import html
import re


register = template.Library()


@register.filter
def unes_ht(text):
    tex = text.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '"').replace('&#x27;', "'") 
    return tex
                  


@register.filter
def es_ht(text):
    # tex = text.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '"').replace('&#39;', "'") 
    pattern = re.compile('<.*?>')
    tex = re.sub(pattern, '', text)
    return tex
                   

@register.filter
def hthtag(value):
    htht = value.replace('1#', '<h1>').replace('2#', '<h2>').replace('3#', '<h3>')\
        .replace('#1', '</h1>').replace('#2', '</h2>').replace('#3', '</h3>').replace('/*', '<center>')\
        .replace('u#', '</ul>').replace('#u', '</ul>').replace('#o', '<ol>').replace('o#', '</ol>')\
        .replace('*/', '</center>').replace('#l', '<li>').replace('l#', '</li>')
    return htht

@register.filter
def urp(value):
    re = value.replace(' ', '-').replace(',', '-').replace('/', ' ').replace('%', '=')
    return re

@register.filter
def urlpl(value):
    # re = value.replace(' ', '-').replace(',', '-').replace('/', ' ').replace('%', '=')
    re = slugify(value, allow_unicode=True)
    return re

@register.filter
def filus(value):
    es = value.replace('<a', '<a id="link-text" target="_blank"' )
    return es
    
@register.filter
def da(value):
    ca = value.replace('minutes', 'mins').replace('minute', 'min').replace('hours', 'hrs').replace('hour', 'hr')\
        .replace('day', 'd').replace('days', 'ds').replace('week', 'wk').replace('weeks', 'wks')\
        .replace('month', 'mo').replace('months', 'mo').replace('week', 'yr').replace('weeks', 'yrs')
    return ca

@register.filter
def day(value):
	day = datetime.date.today().day
	month = datetime.date.today().month
	year = datetime.date.today().year

	array = {
		1: 'Jan.',
		2: 'Feb.',
		3: 'March',
		4: 'April',
		5: 'May',
		6: 'June',
		7: 'July',
		8: 'Aug.',
		9: 'Sept.',
		10: 'Oct.',
		11: 'Nov.',
		12: 'Dec.'
	}

	dati = f'{array[month]} {day}, {year}'
	yesterday = f'{array[month]} {day-1}, {year}'
	dd = f'{array[month]} {0}, {year}'

	if value != '':
		if value == dati:
			return "Today"
		elif value == yesterday or yesterday == dd:
			return "Yesterday"
		else:
			return value


def round_num(n, decimal=2):
    n=Decimal(n)
    return n.to_integral() if n == n.to_integral() else round(n.normalize(), decimal)


@register.filter
def conv(n, decimal=2):

    #60 sufixes
    sufixes = [ "", "K", "M", "B", "T", "Qa", "Qu", "S", "Oc", "No",
                "D", "Ud", "Dd", "Td", "Qt", "Qi", "Se", "Od", "Nd","V",
                "Uv", "Dv", "Tv", "Qv", "Qx", "Sx", "Ox", "Nx", "Tn", "Qa",
                "Qu", "S", "Oc", "No", "D", "Ud", "Dd", "Td", "Qt", "Qi",
                "Se", "Od", "Nd", "V", "Uv", "Dv", "Tv", "Qv", "Qx", "Sx",
                "Ox", "Nx", "Tn", "x", "xx", "xxx", "X", "XX", "XXX", "END"]

    sci_expr = [1e0, 1e3, 1e6, 1e9, 1e12, 1e15, 1e18, 1e21, 1e24, 1e27,
                1e30, 1e33, 1e36, 1e39, 1e42, 1e45, 1e48, 1e51, 1e54, 1e57,
                1e60, 1e63, 1e66, 1e69, 1e72, 1e75, 1e78, 1e81, 1e84, 1e87,
                1e90, 1e93, 1e96, 1e99, 1e102, 1e105, 1e108, 1e111, 1e114, 1e117,
                1e120, 1e123, 1e126, 1e129, 1e132, 1e135, 1e138, 1e141, 1e144, 1e147,
                1e150, 1e153, 1e156, 1e159, 1e162, 1e165, 1e168, 1e171, 1e174, 1e177]
    minus_buff = n
    n=abs(n)
    for x in range(len(sci_expr)):
        try:
            if n >= sci_expr[x] and n < sci_expr[x+1]:
                sufix = sufixes[x]
                if n >= 1e3:
                    num = str(round_num(n/sci_expr[x], decimal))
                else:
                    num = str(n)
                return num + sufix if minus_buff > 0 else "-" + num + sufix
        except IndexError:
            print("You've reached the end")

@register.filter
def tra(value, lang):
    #translator = Translator(to_lang='en')
    #translation = translator.translate(value)
    emt = ''
    #tran = Translator().translate(text=value, dest='es').text   and value.isalpha()
    if value != '':
        tran = GoogleTranslator(source='auto', target=lang).translate(value)
        return tran
    return value


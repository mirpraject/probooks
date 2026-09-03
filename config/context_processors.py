from django.conf import settings


from datetime import date

def theme(request):
    theme_cookie = request.COOKIES.get('theme')
    if theme_cookie:
        return {'theme': theme_cookie}
    
    month = date.today().month
    if month in (3, 4, 5):
        default_theme = 'spring'
    elif month in (6, 7, 8):
        default_theme = 'summer'
    elif month in (9, 10, 11):
        default_theme = 'autumn'
    else:
        default_theme = 'winter'
        
    return {'theme': default_theme}


def current_language(request):
    lang = request.COOKIES.get('django_language', '')
    if not lang:
        lang = getattr(request, 'LANGUAGE_CODE', settings.LANGUAGE_CODE)
    return {'current_language': lang}

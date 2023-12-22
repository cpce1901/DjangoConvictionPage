from .base import *

DEBUG = False

ALLOWED_HOSTS = ['146.190.121.6', 'convictionic.cl', 'www.convictionic.cl']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "convprod",  # Nombre DB
        "USER": "cpce1901",  # Nombre usuario
        "PASSWORD": "cpce1901",  # Password
        "HOST": "localhost",
        "PORT": "3306",
        "OPTIONS": {
            "sql_mode": "STRICT_TRANS_TABLES",
        },
    }
}

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    )
}


STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'

# Llave sitio
RECAPTCHA_PUBLIC_KEY = "6LfctzkpAAAAAHMylvs6cCG0m96sOdvVQQvT1Epa"
# Llave secreta
RECAPTCHA_PRIVATE_KEY = "6LfctzkpAAAAAG33fOS0vYOuVRvEU6j9SNWHoblY"

RECAPTCHA_ERROR_MSG = {
    "required": "Porfavor completa la verificación...",
}
from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "convdev",  # Nombre DB
        "USER": "root",  # Nombre usuario
        "PASSWORD": "cpce1901",  # Password
        "HOST": "localhost",
        "PORT": "3306",
        "OPTIONS": {
            "sql_mode": "STRICT_TRANS_TABLES",
        },
    }
}

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static/"]


MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media_local/"

# Llave sitio
RECAPTCHA_PUBLIC_KEY = "6LfY3TgpAAAAAO-2ig8wpR7qgAWP5IIrTX7vunOB"
# Llave secreta
RECAPTCHA_PRIVATE_KEY = "6LfY3TgpAAAAANOcOOl5qxdETl4ZHqzA3dBrMSLJ"


RECAPTCHA_ERROR_MSG = {
    "required": "Porfavor completa la verificación...",
}


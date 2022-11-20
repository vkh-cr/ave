from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-ss8wu03d6yuwj+(rv8kk3p-=sqa)jxpj_dx)&)ibets%@08-&e"

INSTALLED_APPS = INSTALLED_APPS + [
    "debug_toolbar",
]

MIDDLEWARE = [
    # "debug_toolbar.middleware.DebugToolbarMiddleware",
    "strawberry_django_plus.middlewares.debug_toolbar.DebugToolbarMiddleware",
] + MIDDLEWARE

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass

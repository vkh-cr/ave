from .env import *

INSTALLED_APPS = [
    "apps.core",
    "apps.av",
    "apps.imports",
    "apps.people",
    "website",
    # Wagtail
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail.contrib.modeladmin",
    "wagtail.contrib.styleguide",
    "wagtail",
    "modelcluster",
    "taggit",
    "wagtailmenus",
    # Third-party apps
    "django_extensions",
    "strawberry.django",
    "strawberry_django_plus",
    "strawberry_django_jwt.refresh_token",
    # Django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

ROOT_URLCONF = "av_backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "av_backend" / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "wagtailmenus.context_processors.wagtailmenus",
            ],
        },
    },
]

WSGI_APPLICATION = "av_backend.wsgi.application"


DATABASES = {
    "default": env.db("DATABASE_URL", default=f"sqlite:///{BASE_DIR}/db.sqlite3"),
}

AUTHENTICATION_BACKENDS = [
    "strawberry_django_jwt.backends.JSONWebTokenBackend",
    "django.contrib.auth.backends.ModelBackend",
]


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


TIME_ZONE = "UTC"
USE_TZ = True

LANGUAGE_CODE = "cs"
USE_I18N = True
USE_L10N = True

LOCALE_PATHS = [
    PROJECT_DIR / "locale",
]


STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATICFILES_DIRS = [
    PROJECT_DIR / "static",
]

# STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

STATIC_ROOT = BASE_DIR / "static"
STATIC_URL = "/static/"

MEDIA_ROOT = env.path("MEDIA_ROOT", default=(BASE_DIR / "media"))
MEDIA_URL = "/media/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = "core.User"

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Wagtail
WAGTAIL_SITE_NAME = "AV CMS"
WAGTAILADMIN_BASE_URL = "http://example.com"

WAGTAIL_USER_EDIT_FORM = "apps.core.forms.CustomUserEditForm"
WAGTAIL_USER_CREATION_FORM = "apps.core.forms.CustomUserCreationForm"
WAGTAIL_USER_CUSTOM_FIELDS = [
    # "country",
    # "status",
]

WAGTAIL_ALLOW_UNICODE_SLUGS = False
TAGGIT_CASE_INSENSITIVE = True

# Allow uploading of 100MB files
WAGTAILIMAGES_MAX_UPLOAD_SIZE = 100 * 1024 * 1024
# New users with a blank password will need to reset their password first
WAGTAILUSERS_PASSWORD_REQUIRED = False

WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
    }
}

# Backend settings
GOOGLE_APIS_CREDENTIALS_FILE = env.path(
    "GOOGLE_APIS_CREDENTIALS_FILE", default="/dev/null"
)
AV_TEAM_SHEET_ID = env.str("AV_TEAM_SHEET_ID", default="")

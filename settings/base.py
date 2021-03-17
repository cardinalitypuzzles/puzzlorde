"""
Django settings for puzzlord project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
import datetime
import os

from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", os.getenv("SECRET_KEY"))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [".hunt.superteamaweso.me"]


# Application definition

INSTALLED_APPS = [
    "puzzle_editing.apps.PuzzleEditingConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.humanize",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "puzzlord.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "puzzlord.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.normpath(os.path.join(BASE_DIR, "static"))


LOGIN_URL = "/login"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

EMAIL_USE_TLS = True
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_SUBJECT_PREFIX = "[SHA PUZZLORD] "
EMAIL_HOST_USER = "shapuzzlord@gmail.com"
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")

# Writes email to stdout instead of sending a real email
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "django": {"format": "%(asctime)s [%(levelname)s] %(module)s\n%(message)s"},
        "puzzles": {"format": "%(asctime)s [%(levelname)s] %(message)s"},
    },
    "handlers": {
        "django": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": os.getcwd() + "/logs/django.log",
            "formatter": "django",
        },
        "puzzle": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": os.getcwd() + "/logs/puzzle.log",
            "formatter": "puzzles",
        },
        "request": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": os.getcwd() + "/logs/request.log",
            "formatter": "puzzles",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["django"],
            "level": "DEBUG",
            "propagate": True,
        },
        "puzzles.puzzle": {
            "handlers": ["puzzle"],
            "level": "DEBUG",
            "propagate": False,
        },
        "puzzles.request": {
            "handlers": ["request"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}

# only if you want to do postprodding
HUNT_REPO = "/srv/FIXME/"

HUNT_TIME = datetime.datetime(
    year=2021,
    month=1,
    day=15,
    hour=17,
    minute=0,
    second=0,
    microsecond=0,
    tzinfo=datetime.timezone.utc,
)

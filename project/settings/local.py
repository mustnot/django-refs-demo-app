from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": env("POSTGRES_HOST"),
        "NAME": env("POSTGRES_NAME"),
        "USER": env("POSTGRES_USER"),
        "PORT": env("POSTGRES_POST", default=5432),
        "PASSWORD": env("POSTGRES_PASSWORD"),
    }
}

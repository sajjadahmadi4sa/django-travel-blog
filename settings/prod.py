from .base import *
import os

SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = False

ALLOWED_HOSTS = [
    'YOUR-DOMAIN.COM',
    'WWW.YOUR-DOMAIN.COM',
]


INSTALLED_APPS = [
    app for app in INSTALLED_APPS
    if app != 'debug_toolbar'
]


MIDDLEWARE = [
    middleware for middleware in MIDDLEWARE
    if middleware != 'debug_toolbar.middleware.DebugToolbarMiddleware'
]
from .base import *
import os

SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = False

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'travel-blog.ir',
    'www.travel-blog.ir',
]

INSTALLED_APPS = [
    app for app in INSTALLED_APPS
    if app != 'debug_toolbar'
]


MIDDLEWARE = [
    middleware for middleware in MIDDLEWARE
    if middleware != 'debug_toolbar.middleware.DebugToolbarMiddleware'
]
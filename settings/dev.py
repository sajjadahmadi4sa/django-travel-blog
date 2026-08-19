from .base import *
import os

SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = True

ALLOWED_HOSTS = []


INTERNAL_IPS = [
    '127.0.0.1',
]
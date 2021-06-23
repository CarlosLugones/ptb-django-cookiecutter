from .base import *

DEBUG = False

# You can use sqlite3 or another DB on production. It's up to you
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

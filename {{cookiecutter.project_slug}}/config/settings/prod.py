from .base import *

DEBUG = False

# you should put your host here if you think set in production the web app
ALLOWED_HOSTS = ["*"]

# You can use sqlite3 or another DB on production. It's up to you
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# security config
# SECURE_HSTS_SECONDS = 3600  # 1 hours. 31536000 seconds = 1 year
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_REFERRER_POLICY = 'origin'
SECURE_HSTS_PRELOAD = True  # Without this, your site cannot be submitted to the browser preload list.


# cookies
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 3600  # 1 hour only

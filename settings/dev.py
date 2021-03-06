from .base import *

SECRET_KEY = os.environ.get('SECRET_KEY', default='foo')

DEBUG = int(os.environ.get('DEBUG', default=1))

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']

STATIC_URL = '/static/'

MEDIA_URL = 'media/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

LOGIN_REDIRECT_URL = 'admin/login'


import django_on_heroku
from decouple import config

from .base import *

SECRET_KEY = config('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = [
    'https://sentir-humano.herokuapp.com/',
    'https://sentir-s3-bucket.s3.amazonaws.com/'
    'https://soysentirhumano.com/'
    'https://82.180.137.61/'
    ]
CSRF_TRUSTED_ORIGINS = ['https://*.herokuapp.com/', 'https://*.127.0.0.1', 'https://*.soysentirhumano.com/']

# Amazon S3 Settings

USE_S3 = os.getenv('USE_S3') == 'TRUE'

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')

AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')

AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')

AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

AWS_DEFAULT_ACL = 'public-read'

AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}

AWS_LOCATION = 'static'

AWS_QUERYSTRING_AUTH = False

AWS_HEADERS = {'Access-Control-Allow-Origin': '*'}

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'

STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'

MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'


# Heroku Logging

DEBUG_PROPAGATE_EXCEPTIONS = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'MYAPP': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}


# Heroku Settings
django_on_heroku.settings(locals(), staticfiles=False)
del DATABASES['default']['OPTIONS']['sslmode']
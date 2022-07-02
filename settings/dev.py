from .base import *

SECRET_KEY = '21nbd3$ef+jmvr6$3dku0fwgke1*2%2^8+fzlc7r#tktya*n@d'

DEBUG = False

ALLOWED_HOSTS = ['*']

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')

MEDIA_URL = 'media/'

MEDIA_ROOT = BASE_DIR / 'media'

LOGIN_REDIRECT_URL = 'admin/login'


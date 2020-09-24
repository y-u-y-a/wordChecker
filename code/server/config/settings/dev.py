from .base import *

ALLOWED_HOSTS = ['*']

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test_database',
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': os.environ['MYSQL_DATABASE'],
#         'HOST': os.environ['MYSQL_HOST'],
#         'PORT': os.environ['MYSQL_PORT'],
#         'USER': os.environ['MYSQL_USER'],
#         'PASSWORD': os.environ['MYSQL_PASSWORD'],
#         'OPTIONS': {
#             'charset': 'utf8mb4',
#         },
#     }
# }
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'DATABASE_NAME',
#         'HOST': '127.0.0.1',
#         'PORT': 4306,
#         'USER': 'root',
#         'PASSWORD': 'root',
#         'OPTIONS': {
#             'charset': 'utf8mb4',
#         },
#     }
# }

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, '_media')
MEDIA_URL = '/media/'

# Preflightを返すドメインを指定
CORS_ALLOWED_ORIGINS  = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
]
# Cookieを含ませるか？
CORS_ALLOW_CREDENTIALS = True
INSTALLED_APPS.append('corsheaders')
MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware')

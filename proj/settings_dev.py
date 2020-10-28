from .settings import *

DEBUG = True
ALLOWED_HOSTS = ['*']
INTERNAL_IPS = ('127.0.0.1', 'localhost',)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sidia',
        'USER': 'postgres',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '5433',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'NAME': 'sidia',
#         'CLIENT': {
#                 'host': '127.0.0.1',
#                 'port': 27016,
#                 'username': 'root',
#                 'password': 'sidia',
#             },
#     }
# }

MONGO_HOST = 'localhost'
MONGO_PORT = 27016
MONGO_USER = 'root'
MONGO_PASSWORD = 'sidia'
MONGO_DB = 'tickets'

AUTH_PASSWORD_VALIDATORS = []

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'Suporte  <suporte@sidia.com.br>'
from .settings import *

DEBUG = False
ALLOWED_HOSTS = ['*']
INTERNAL_IPS = ('127.0.0.1', 'localhost',)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sidia',
        'USER': 'postgres',
        'PASSWORD': 'root',
        'HOST': 'db_prod',
        'PORT': '5432',
    }
}


MONGO_HOST = 'mongo_db'
MONGO_PORT = 27017
MONGO_USER = 'root'
MONGO_PASSWORD = 'sidia'
MONGO_DB = 'tickets'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'suporte@sidia.com.br'
EMAIL_HOST_PASSWORD = 'senha'
DEFAULT_FROM_EMAIL = 'Suporte  <suporte@sidia.com.br>'
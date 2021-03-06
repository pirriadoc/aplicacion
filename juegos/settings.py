"""
Django settings for juegos project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""
from django.utils.translation import ugettext_lazy as _
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGIN_REDIRECT_URL ='/'
LOGIN_URL ='/accounts/login'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ndkxerwoo_n269v#z=_+kh-a@9u(p0^(-aifcd_p(%q9l_*$0%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'comven',
    'registration',
    'bootstrap3'
)

ACCOUNT_ACTIVATION_DAYS = 7 # una semana para activar la cuenta
REGISTRATION_AUTO_LOGIN = True # al pinchar en el enlace enviado al registrarse el usuario se loguea automaticamente.

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'juegos.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'juegos.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

  DATABASES = {
     'default': {
-        'ENGINE': 'django.db.backends.sqlite3',
-        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.posgresql',
#        'NAME': 'posgresql',
#        'USER': 'javier'
#        'PASSWORD': 'javier'
#        'HOST': ''
#    }
#}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('de', _('German')),
    ('en', _('English')),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

import ldap
from django_auth_ldap.config import LDAPSearch, PosixGroupType

AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)

AUTH_LDAP_SERVER_URI = "ldap://192.168.10.22"

AUTH_LDAP_BIND_DN = "cn=Directory Manager"
AUTH_LDAP_BIND_PASSWORD = "secret"
AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=People,dc=example,dc=com",
    ldap.SCOPE_SUBTREE, "(uid=%(user)s)")

AUTH_LDAP_GROUP_SEARCH = LDAPSearch("ou=Groups,dc=example,dc=com",
    ldap.SCOPE_SUBTREE, "(objectClass=PosixGroup)"
)
AUTH_LDAP_GROUP_TYPE = PosixGroupType(name_attr="cn")

AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    "is_active": "uid=tmorris,ou=People,dc=example,dc=com",
    "is_staff": "uid=tmorris,ou=People,dc=example,dc=com",
    "is_superuser": "uid=tmorris,ou=People,dc=example,dc=com"
}

AUTH_LDAP_FIND_GROUP_PERMS = True

AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn"
}

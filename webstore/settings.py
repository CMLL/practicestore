import os
import sys
# Import some utility functions
from os.path import abspath, basename, dirname, join, normpath

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ##### PATH CONFIGURATION ################################

# Fetch project directory
PROJECT_ROOT = dirname(dirname(abspath(__file__)))

# Collect static files here
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

# Collect media files here
MEDIA_ROOT = join(PROJECT_ROOT, 'media')

# look for static assets here
STATICFILES_DIRS = (
    join(PROJECT_ROOT, 'media'),
)

# look for templates here
# This is an internal setting, used in the TEMPLATES directive
PROJECT_TEMPLATES = (
    join(PROJECT_ROOT, 'templates'),
)

# Add apps/ to the Python path
sys.path.append(normpath(join(PROJECT_ROOT, 'apps')))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ny)&4&_r0b62v175%p$t$wdogl7qefo%ci$=n^*)&k_r)@ef(m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

DJANGO_APPS = (
    # 'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

LOCAL_APPS = (
    'apps.users',
)

THIRTY_APPS = (
    'rest_framework',
    'apps.users.apps.UsersConfig',
    'crispy_forms',
)

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRTY_APPS

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ),
}


ROOT_URLCONF = 'webstore.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': PROJECT_TEMPLATES,
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

WSGI_APPLICATION = 'webstore.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'store_db',
        'USER': os.environ.get('MYSQL_USERNAME'),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '3306'
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
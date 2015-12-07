"""
Django settings for csp project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import logging
import os, django
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v1*ah#)@vyov!7c@n&c2^-*=8d)-d!u9@#c4o*@k=1(1!jul6&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = DEBUG
APPEND_SLASH = True

# Allow all host headers
ALLOWED_HOSTS = ['*']

REST_FRAMEWORK = {
    # Use hyperlinked styles by default.
    # Only used if the `serializer_class` attribute is not set on a view.
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'oauth2_provider.ext.rest_framework.OAuth2Authentication',),
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
        # 'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    )
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    # 'PAGE_SIZE': 100
}

OAUTH2_PROVIDER = {
    # this is the list of available scopes
    'SCOPES': {'read': 'Read scope', 'write': 'Write scope'}
}

OAUTH2_PROVIDER_APPLICATION_MODEL = 'oauth2_provider.Application'
MIGRATION_MODULES = {
    'oauth2_provider': 'crowdsourcing.migrations.oauth2_provider',
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'django.contrib.sessions',
    'django.contrib.postgres',
    'compressor',
    'rest_framework',
    'oauth2_provider',
    'crowdsourcing'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    # 'crowdsourcing.middleware.csrf.CustomCsrfViewMiddleware',
    'crowdsourcing.middleware.active.CustomActiveViewMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'csp.urls'
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'static/django_templates')],
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

WSGI_APPLICATION = 'csp.wsgi.application'

DATABASES = {
    'default': dj_database_url.config()
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True

# Email
EMAIL_HOST = 'localhost'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_ENABLED = True
EMAIL_SENDER = 'daemo@cs.stanford.edu'
EMAIL_SENDER_DEV = 'crowdsourcing.platform.demo@gmail.com'
EMAIL_SENDER_PASSWORD_DEV = 'crowdsourcing.demo.2015'
SENDGRID_API_KEY = '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'

# Others
REGISTRATION_ALLOWED = False
PASSWORD_RESET_ALLOWED = True

LOGIN_URL = '/login'
# SESSION_ENGINE = 'redis_sessions.session'

# Security
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
PYTHON_VERSION = 2
try:
    from local_settings import *
except Exception as e:
    pass

GRAPH_MODELS = {
    'all_applications': True,
    'group_models': True,
}

if float(django.get_version()) < 1.8:
    FIXTURE_DIRS = (
        os.path.join(BASE_DIR, 'fixtures')
    )

USERNAME_MAX_LENGTH = 30

# Google Drive
GOOGLE_DRIVE_CLIENT_ID = '960606345011-3bn8sje38i9c0uo8p87ln6tfb2dhco9v.apps.googleusercontent.com'
GOOGLE_DRIVE_CLIENT_SECRET = 'v-gWQKOmuAhTmbJ5REwH-V_1'
GOOGLE_DRIVE_OAUTH_SCOPE = 'https://www.googleapis.com/auth/drive'
GOOGLE_DRIVE_REDIRECT_URI = 'http://localhost:8000/api/google-auth-finish'

# Dropbox
DROPBOX_APP_KEY = '__KEY__'
DROPBOX_APP_SECRET = '__SECRET__'
DROPBOX_REDIRECT_URI = 'http://localhost:8000/api/dropbox-auth-finish'

# PayPal
PAYPAL_API_URL = 'https://api.sandbox.paypal.com'
PAYPAL_CLIENT_ID = 'ASMOowufDMA_QZ_XgjbyF4WTzeSGMBJlZq5mefCP02zjWOk92BD2NyrztHZIR_ZGny8qKD4n7SQel2wy'
PAYPAL_CLIENT_SECRET = 'EGhnNaEAUWjLuXLF5jLuR1sOlhi0CFtT9hqIuGOvKtFUZhHiVQH046l2PxhzvvN5Nw9aU4ZoE_HHMgoD'

# Secure Settings
if not DEBUG:
    # Honor the 'X-Forwarded-Proto' header for request.is_secure()
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_FRAME_DENY = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SECURE_SSL_REDIRECT = True
    CSRF_TRUSTED_ORIGINS = [
        'daemo.herokuapp.com', 'daemo.stanford.edu',
        'daemo-staging.herokuapp.com', 'daemo-staging.stanford.edu'
    ]

# MANAGER CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ("Daemo", 'daemo@cs.stanford.edu')  # add more team members
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

# LOGGING CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'suppress_deprecated': {
            '()': 'csp.settings.SuppressDeprecated'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_false', 'suppress_deprecated'],
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.security': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'py.warnings': {
            'handlers': ['console'],
        },
    }
}


class SuppressDeprecated(logging.Filter):
    def filter(self, record):
        warnings = [
            'RemovedInDjango18Warning',
            'RemovedInDjango19Warning'
        ]

        # Return false to suppress message.
        return not any([warn in record.getMessage() for warn in warnings])

from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = env.bool("DEBUG", True)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['nuranbot.applikuapp.com'])

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler'
#         },
#     },
#     'loggers': {
#         '': {  # 'catch all' loggers by referencing it with the empty string
#             'handlers': ['console'],
#             'level': 'DEBUG',
#         },
#     },
# }
####################### Wsgi Applicaton - Producton Only #######################

WSGI_APPLICATION = 'django-backend.wsgi.application'

####################### DON'T DUPLICATE APP #######################
# DJANGO Project Apps Managments

DJANGO_APPS += [

]

THIRD_PARTY_APPS = [
    
]

LOCAL_APPS = [
    'apps.authentication.apps.AuthenticationConfig',
    'apps.home.apps.HomeConfig',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
###################################################################
# Database

# Databases
DATABASES = {
    "default": env.db("DATABASE_URL")
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True
DATABASES["default"]["CONN_MAX_AGE"] = env.int("CONN_MAX_AGE", default=60)
###################################################################

DOMAIN = ('globador.com')
SITE_NAME = ('Globador')

################################################################
# Authentication Backends
AUTHENTICATION_BACKENDS = (
    # Django
    'django.contrib.auth.backends.ModelBackend',
)
###################################################################

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
# Local
STATICFILES_DIRS = [
    os.path.join(BASE_DIR.parent, 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR.parent, 'static/build')

# Media Config
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR.parent, 'media')

CSRF_TRUSTED_ORIGINS =['https://nuranbot.applikuapp.com']
# CSRF_TRUSTED_ORIGINS =os.getenv("CSRF_TRUSTED_ORIGINS")


# # Static files (CSS, JavaScript, Images)
# # Production
# LINODE_BUCKET=''
# LINODE_BUCKET_REGION='eu-central-1'
# LINODE_BUCKET_ACCESS_KEY=''
# LINODE_BUCKET_SECRET_KEY=''

# # LINODE_BUCKET = str(os.getenv('LINODE_BUCKET'),)
# # LINODE_BUCKET_REGION = str(os.getenv('LINODE_BUCKET_REGION'),)
# # LINODE_BUCKET_ACCESS_KEY = str(os.getenv('LINODE_BUCKET_ACCESS_KEY'),)
# # LINODE_BUCKET_SECRET_KEY = str(os.getenv('LINODE_BUCKET_SECRET_KEY'),)


# AWS_ACCESS_KEY_ID = LINODE_BUCKET_ACCESS_KEY
# AWS_SECRET_ACCESS_KEY = LINODE_BUCKET_SECRET_KEY
# AWS_S3_REGION_NAME = LINODE_BUCKET_REGION
# AWS_S3_USE_SSL = True
# AWS_STORAGE_BUCKET_NAME = LINODE_BUCKET
# AWS_S3_ENDPOINT_URL = f'https://{LINODE_BUCKET_REGION}.linodeobjects.com'

# # AWS_DEFAULT_ACL="authenticated-read" # Make uploaded files readable for authenticated
# AWS_DEFAULT_ACL="public-read" # Make uploaded files public

# STATIC_URL = '/static/'
# # STATIC_URL = f'https://{LINODE_BUCKET_REGION}.linodeobjects.com/{LINODE_BUCKET}/static/'
# MEDIA_URL = f'https://{LINODE_BUCKET_REGION}.linodeobjects.com/{LINODE_BUCKET}/media/'

# # MEDIA_URL = f'https://{LINODE_BUCKET}.{LINODE_BUCKET_REGION}.linodeobjects.com/media/'

# DEFAULT_FILE_STORAGE = 'django-backend.storage_backends.MediaStorage'
# # DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# STATIC_ROOT = os.path.join(BASE_DIR.parent, 'static/build')
# # PDF_ROOT = os.path.join(BASE_DIR.parent, 'invoice/build')
# # STATICFILES_STORAGE = 'django-backend.storage_backends.StaticStorage'
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# # STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage" #NoT cashed 

# # AWS_LOCATION = "static"
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR.parent, "static"),
# ]
from .settings.base import *


# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
# DEBUG = env.bool('DEBUG', default=True)
DEBUG = False

# ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split(",")
# ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['localhost', '127.0.0.1', 'muhammedelassii.pythonanywhere.com'])

ALLOWED_HOSTS = [
    "muhammedelassii.pythonanywhere.com",
    "globador-frontend.vercel.app",
    "localhost",
    "127.0.0.1",
    "globadorvet",
    "globadorvet.com",
    "www.globadorvet.com",
    "globador.shop",
    "www.globador.shop",
]

CORS_ALLOWED_ORIGINS = [
    "https://muhammedelassii.pythonanywhere.com",
    "https://globador-frontend.vercel.app/",
    "https://www.globadorvet.com/",
    "http://www.globadorvet.com/",
    "https://globador.shop/",
    "http://globador.shop/",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

####################### DON'T DUPLICATE APP #######################
# DJANGO Project Apps Managments

LOCAL_APPS = [
    'apps.authentication.apps.AuthenticationConfig',
    'apps.home.apps.HomeConfig',
]


DJANGO_APPS += [

]

THIRD_PARTY_APPS = [
    
]


INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

###################################################################
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
###################################################################
# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'globador_db.sqlite3'),
        # 'NAME': 'globador_db', # This is where you put the name of the db file. 
        # If one doesn't exist, it will be created at migration time.
    }
}

# POSTGRES_NAME='globador'
# POSTGRES_USER='postgres'
# POSTGRES_PASSWORD='admin'
# POSTGRES_HOST='localhost'
# POSTGRES_PORT='5432'
# POSTGRES_DB='globador'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': POSTGRES_NAME,
#         'USER': POSTGRES_USER,
#         'PASSWORD': POSTGRES_PASSWORD,
#         'HOST': POSTGRES_HOST,
#         'PORT': POSTGRES_PORT,
#     }
# }
###################################################################

DOMAIN = ('https://muhammedelassii.pythonanywhere.com')
SITE_NAME = ('Globador')

################################################################
# Django Urls Append Slash Configuration
APPEND_SLASH = True

################################################################
# Authentication Backends
AUTHENTICATION_BACKENDS = (
    # Django
    'django.contrib.auth.backends.ModelBackend',
)
################################################################

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

CSRF_TRUSTED_ORIGINS = [
    'https://muhammedelassii.pythonanywhere.com',
    'http://127.0.0.1:8000',  # Replace with your exact development URL
    'https://localhost:8080',  # Include any other trusted URLs using scheme (http:// or https://)
    'https://globador.shop',
    'http://globador.shop',
    'https://www.globadorvet.com',
    'http://www.globadorvet.com',
    "https://globador-frontend.vercel.app/",
]
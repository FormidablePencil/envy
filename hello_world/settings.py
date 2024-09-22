import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Define BASE_DIR

ALLOWED_HOSTS = ['*']  # Allow all hosts for development purposes
DEBUG = True  # Set DEBUG to True for development
SECRET_KEY = 'your-secret-key'  # Set a secret key for your application
ROOT_URLCONF = 'hello_world.urls'  # Set the root URL configuration
CORS_ALLOWED_ORIGINS = [
    'http://localhost:8000',  # Add your allowed origins here
]
INSTALLED_APPS = [
    'corsheaders',  # Add this line to include django-cors-headers
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
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
STATIC_URL = '/static/'  # Set the URL for static files

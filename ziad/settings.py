import os
from pathlib import Path
import dj_database_url

# إعداد المسارات الأساسية - قمنا بتعديله ليتناسب مع هيكل مجلداتك
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# مفتاح الأمان
SECRET_KEY = 'django-insecure-suhail-yemen-pharmacy-project-key'

# تفعيل وضع التصحيح (اجعله True حالياً لنرى الخطأ إن وجد)
DEBUG = True

# السماح للرابط الخاص بك بالعمل
ALLOWED_HOSTS = ['ziad1-e65w.onrender.com', 'localhost', '127.0.0.1', '*']

# التطبيقات المثبتة
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic', 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# تأكد أن هذه المسارات مطابقة لأسماء مجلداتك في GitHub
ROOT_URLCONF = 'ziad.ziad.urls'
WSGI_APPLICATION = 'ziad.ziad.wsgi.application'

# إعداد القوالب
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

# قاعدة البيانات
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3'),
        conn_max_age=600
    )
}

# إعدادات الوقت واللغة (صنعاء، اليمن)
LANGUAGE_CODE = 'ar-ye'
TIME_ZONE = 'Asia/Aden'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# الملفات الثابتة
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

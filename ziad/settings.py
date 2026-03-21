import os
from pathlib import Path
import dj_database_url

# إعداد المسارات الأساسية
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# مفتاح الأمان (لا تشاركه مع أحد في مشروع حقيقي)
SECRET_KEY = 'django-insecure-suhail-yemen-pharmacy-project-key'

# تفعيل وضع التصحيح (اجعله False عند الانتهاء تماماً)
DEBUG = True

# السماح لجميع الروابط بالوصول (ضروري لـ Render)
ALLOWED_HOSTS = ['*']

# التطبيقات المثبتة
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic', # لإدارة ملفات التصميم
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # ضروري جداً لظهور الصور والتنسيقات
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# المسار الصحيح للملفات الأساسية
ROOT_URLCONF = 'ziad.ziad.urls'
WSGI_APPLICATION = 'ziad.ziad.wsgi.application'

# إعداد القوالب (Templates) للبحث عن ملف inventory.html
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

# ربط قاعدة البيانات بموقع Render (PostgreSQL) أو استخدام SQLite مؤقتاً
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3'),
        conn_max_age=600
    )
}

# إعدادات ملفات اللغة والوقت
LANGUAGE_CODE = 'ar-ye'
TIME_ZONE = 'Asia/Aden'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# إعدادات الملفات الثابتة (Static Files) لـ Render
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

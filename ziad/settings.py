import os
from pathlib import Path
import dj_database_url

# BASE_DIR يشير الآن للمجلد الرئيسي للمستودع الذي يحتوي على templates و manage.py
BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = 'suhail-pharmacy-secure-key-2026'

# تفعيل DEBUG يساعدك على رؤية الأخطاء أثناء البناء
DEBUG = True

ALLOWED_HOSTS = [
    'ziad1-e65w.onrender.com', 
    'ziad-3.onrender.com', 
    'ziad-4.onrender.com', 
    'localhost', 
    '127.0.0.1', 
    '*'
]

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

# تم تعديل هذا المسار ليتناسب مع مجلد ziad الفرعي
ROOT_URLCONF = 'ziad.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # توجيه النظام للبحث عن المجلد في المكان الصحيح بناءً على BASE_DIR الجديد
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

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
    )
}

LANGUAGE_CODE = 'ar-ye'
TIME_ZONE = 'Asia/Aden'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# إعدادات تسجيل الدخول والروابط
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'inventory'
LOGOUT_REDIRECT_URL = 'login'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

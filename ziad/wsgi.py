import os
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ziad.settings')

application = get_wsgi_application()

# تنفيذ migrate تلقائياً عند التشغيل
try:
    print("جاري تهيئة قاعدة البيانات...")
    call_command('migrate', interactive=False)
except Exception as e:
    print(f"خطأ في التهيئة: {e}")

import os
from django.core.wsgi import get_wsgi_application

# تم تعديل المسار ليتناسب مع هيكلية المجلدات لديك
# المجلد الرئيسي (ziad) -> المجلد الفرعي (ziad) -> ملف الإعدادات (settings)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ziad.settings')

application = get_wsgi_application()

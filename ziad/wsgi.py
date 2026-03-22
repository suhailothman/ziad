import os
from django.core.wsgi import get_wsgi_application

# تأكد أن المسار يطابق إعداداتك (ziad.settings)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ziad.ziad.settings')

application = get_wsgi_application()

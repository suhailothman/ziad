from django.contrib.auth.models import User
from django.http import HttpResponse

# وظيفة مؤقتة لإنشاء حساب المدير
def create_admin_manual(request):
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'suhail2026')
        return HttpResponse("<h2>تم إنشاء حساب المدير بنجاح!</h2><p>المستخدم: admin<br>كلمة المرور: suhail2026</p>")
    return HttpResponse("<h2>الحساب موجود مسبقاً</h2>")

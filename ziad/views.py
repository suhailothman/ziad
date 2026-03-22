from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# نظام التسجيل الجديد
def register(request):
    if request.method == 'POST':
        # هنا يتم استقبال بيانات الصيدلية مع التسجيل
        # سنقوم بتطوير نموذج مخصص في المرحلة القادمة
        messages.success(request, 'تم إنشاء الحساب بنجاح، يمكنك الدخول الآن.')
        return redirect('login')
    return render(request, 'register.html')

@login_required
def inventory_view(request):
    # ميزة البحث الذكي
    search_query = request.GET.get('search', '')
    
    # عينة من المخزون (يمكنك تغييرها أو رفع ملف Excel لاحقاً)
    inventory_data = [
        {'id': '101', 'name': 'أوميبرازول 20 ملجم', 'expiry': '2027-05', 'price': 1200},
        {'id': '101', 'name': 'بندول نايت', 'expiry': '2026-10', 'price': 800},
        {'id': '202', 'name': 'أموكسيسيلين 500', 'expiry': '2025-12', 'price': 2500},
    ]
    
    if search_query:
        inventory_data = [item for item in inventory_data if search_query in item['name']]
        
    return render(request, 'inventory.html', {'inventory': inventory_data})

@login_required
def send_order(request):
    if request.method == 'POST':
        # كود إرسال الطلب للأدمن سيتم برمجته هنا
        messages.success(request, 'تم إرسال طلبك بنجاح للأدمن.')
        return redirect('inventory')

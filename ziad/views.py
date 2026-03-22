from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import PharmacyProfile, InventoryItem, Order
from django.contrib import messages
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        # الحصول على البيانات من النموذج
        u_name = request.POST.get('username')
        u_pass = request.POST.get('password')
        p_name = request.POST.get('pharmacy_name')
        loc = request.POST.get('location')
        phone = request.POST.get('manager_phone')
        
        if User.objects.filter(username=u_name).exists():
            messages.error(request, "اسم المستخدم أو الرقم مسجل مسبقاً")
        else:
            user = User.objects.create_user(username=u_name, password=u_pass)
            PharmacyProfile.objects.create(user=user, pharmacy_name=p_name, location=loc, manager_phone=phone)
            login(request, user)
            return redirect('inventory')
    return render(request, 'register.html')

@login_required
def inventory_view(request):
    items = InventoryItem.objects.all()
    # بيانات الصيدلية للترويسة
    profile = PharmacyProfile.objects.get(user=request.user)
    return render(request, 'inventory.html', {'inventory': items, 'profile': profile})

@login_required
def send_order(request):
    if request.method == 'POST':
        # هنا سيتم استقبال الطلبات وتخزينها للأدمن
        messages.success(request, "تم إرسال طلبك بنجاح")
        return redirect('inventory')

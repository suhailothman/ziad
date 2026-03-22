from django.contrib import admin
from django.urls import path
from django.shortcuts import render

# دالة بسيطة لعرض صفحة المخزون مباشرة
def inventory_view(request):
    return render(request, 'inventory.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inventory_view, name='inventory'), # الصفحة الرئيسية هي المخزون
]

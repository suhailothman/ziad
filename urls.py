from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect

# واجهة بسيطة لعرض المخزون والبحث (View)
def inventory_page(request):
    # بيانات تجريبية للمخزن (م1 و م2)
    medicines = [
        {'store': 'م1', 'name': 'بنادول 500 ملجم', 'expiry': '2025-12', 'qty': 100, 'price': 500},
        {'store': 'م2', 'name': 'أموكسيسيلين 250', 'expiry': '2024-06', 'qty': 50, 'price': 1200},
    ]
    query = request.GET.get('q', '')
    if query:
        medicines = [m for m in medicines if query in m['name']]
    
    return render(request, 'inventory.html', {'medicines': medicines, 'query': query})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inventory_page, name='inventory'),
]

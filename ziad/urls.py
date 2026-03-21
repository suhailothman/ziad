from django.contrib import admin
from django.urls import path
from django.shortcuts import render

# دالة عرض المخزون والبحث
def inventory_view(request):
    medicines = [
        {'warehouse': 'م1', 'name': 'بنادول 500 ملجم', 'expiry': '2025-12', 'qty': 100, 'price': 500},
        {'warehouse': 'م2', 'name': 'أموكسيسيلين 250', 'expiry': '2024-06', 'qty': 50, 'price': 1200},
        {'warehouse': 'م1', 'name': 'فيتامين سي', 'expiry': '2026-01', 'qty': 200, 'price': 300},
    ]
    query = request.GET.get('q', '')
    if query:
        medicines = [m for m in medicines if query.lower() in m['name'].lower()]
    
    return render(request, 'inventory.html', {'medicines': medicines, 'query': query})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inventory_view, name='inventory'),
]

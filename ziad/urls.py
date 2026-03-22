from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # مسارات الحسابات
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    
    # الصفحة الرئيسية (المخزون)
    path('', views.inventory_view, name='inventory'),
    
    # مسار إرسال الطلبات
    path('send-order/', views.send_order, name='send_order'),
]

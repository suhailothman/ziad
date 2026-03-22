from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # صفحة الدخول والاشتراك
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    
    # صفحة المخزون والفاتورة
    path('', views.inventory_view, name='inventory'),
    path('send-order/', views.send_order, name='send_order'),
]

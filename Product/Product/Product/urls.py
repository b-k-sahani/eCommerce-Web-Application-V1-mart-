"""Product URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

from Product import settings
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showIndex,name="main"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('admin_login_check/',views.admin_login_check,name="admin_login_check"),
    path('admin_home/',views.admin_home,name="admin_home"),
    path('admin_view_users/',views.admin_view_users,name="admin_view_users"),
    path('admin_view_products/',views.admin_view_products,name="admin_view_products"),
    path('save_product/',views.save_product,name="save_product"),

    path('add_to_cart/',views.add_to_cart,name="add_to_cart"),
    path('in_cart/',views.in_cart,name="in_cart"),
    path('delete_cart/',views.delete_cart,name="delete_cart"),

    path('user_login/', views.user_login, name="user_login"),
    path('user_login_check/', views.user_login_check, name="user_login_check"),
    path('save_user/', views.save_user, name="save_user"),
    path('user_home/', views.user_home, name="user_home"),
    path('user_products/', views.user_products, name="user_products"),
    path('uadd_to_cart/', views.uadd_to_cart, name="uadd_to_cart"),
    path('api/',include('app.api.urls')),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
URL configuration for Project_DB_Django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.urls import path
from django.views.generic import TemplateView
from task1.views import platform_start, games_shop, cart_shop, sign_up_by_html, sign_up_by_django
from task1.views import news


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='second_task/welcome.html')),
    path('platform/', platform_start),
    path('platform/games/', games_shop),
    path('platform/cart/', cart_shop),
    path('sign_up_by_html/', sign_up_by_html),
    path('sign_up_by_django/', sign_up_by_django),
    path('platform/news/', news),
]

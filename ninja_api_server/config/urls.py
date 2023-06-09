"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

# View 함수 + Ninja API
from core.views import *

# static 파일
from django.urls import re_path as url
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    # 메인 화면 = docs
    path('', index, name='index'),

    # Ninja API
    path('api/', api.urls),

    # uvicorn 에서 static 파일 불러오기 (UI 미사용 시 제거 가능)
    url(r'^static/(?P<path>.*)$', serve, {'document_root' : settings.STATIC_ROOT}),
]

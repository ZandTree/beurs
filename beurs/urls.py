"""beurs URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import  routers
from api.account.viewsets import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup-customer/',include('users.urls'))
    
]
# (temp) path for browser api view
urlpatterns +=[
    path('api-auth/', include('rest_framework.urls'))
    ]
# djoser path
urlpatterns +=[
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls')),
]
# other api paths
# urlpatterns +=[
#     path('api/v1/', include(router.urls)),
# ]

#djoser urls
# ************************************
# step N 1: register user

# url: auth/users/
# other features
# url: auth/users/...кучи разных экстра для создания и опереций над юзерами
# smth like: confirm email, reset psw
# step N2
# activate
# auth/users/activate
# http://127.0.0.1:8080/activate/NDM/5ir-d995..


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

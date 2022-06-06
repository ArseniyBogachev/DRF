"""rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework import urls
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from women.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view()),
    # path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/womenlist', WomenAPIListPost.as_view()),
    path('api/v1/womenupdate/<int:pk>/', WomenAPIUpdate.as_view()),
    path('api/v1/womenrelationupdate/<int:women>/', WomenRelationAPIUpdate.as_view()),
    path('api/v1/womendelete/<int:pk>/', WomenAPIDelete.as_view()),
    re_path(r'^auth/', include('djoser.urls')),
    # re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/v1/register', CustomRegistrationView.as_view({'post': 'create'})),
    path(r'auth/', include('djoser.urls.jwt')),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/v1/blacklist/', BlackListAddJWT.as_view(), name='black_list'),
    # path('api/v1/refresh_token/', RefreshJWTView.as_view(), name='black_list'),
    re_path(r'activate/(?P<uid>[\w-]+)/(?P<token>[\w-]+)/$', ActivateJWT.as_view(), name='activation'),
]

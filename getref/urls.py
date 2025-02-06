"""getref URL Configuration

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
from django.contrib.auth.models import User, Group
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path, re_path as url
from django.conf.urls.i18n import i18n_patterns
from getref import settings
from rest_framework import generics, permissions, serializers
from oauth2_provider import urls as oauth2_urls
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from subscriptions.views import create_checkout_session, stripe_config, stripe_webhook

schema_view = get_schema_view(
    openapi.Info(
        title="Get Ref API",
        default_version='v1',
        description="Get Ref is a web-server RESTful ",
        terms_of_service="https://www.google.com/policies/terms/", 
        contact=openapi.Contact(email="alessandro.chiaiese@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    # language
    path('i18n/', include('django.conf.urls.i18n')),
    
    # API 
    path('api/v0/', include('dashboard.api.urls'), name='api_profile'),
    path('api/v0/affiliate/', include('affiliate.api.urls'), name='api_affiliate_v0'),
    path('api/v0/referral/', include('referral.api.urls'), name='api_referral'),

    ## social django
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    
    # accounts 
    path('', include('accounts.urls')),
    
    # health
    path('health/', include('health_check.urls')),
    
    path('config/', stripe_config),
    path('create-checkout-session/', create_checkout_session),
    path('webhook/', stripe_webhook),

    # swagger 
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += i18n_patterns(
    # apps   
    path('', include('dashboard.urls')),
    path('', include('affiliate.urls')), 
    path('', include('referral.urls')),
    path('', include('payments.urls')),
    path('', include('subscriptions.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
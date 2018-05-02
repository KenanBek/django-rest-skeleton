"""Django REST URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.utils.translation import ugettext as _

from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

from demo import api_views as demo_api_views

schema_view = get_schema_view(title=_('DRS API Schema'))

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'categories', demo_api_views.CategoryViewSet)
router.register(r'posts', demo_api_views.PostViewSet)
router.register(r'tags', demo_api_views.TagViewSet)

urlpatterns = [
    # Static home page with links (see settings.TEMPLATES conf)
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    # Link to administration
    url(r'^admin/', admin.site.urls),
    # Link to api
    url(r'^api/', include(router.urls)),
    # Link to api auth
    url(r'^api-auth/', include('rest_framework.urls')),
    # Link to api docs
    url(r'^docs/', include_docs_urls(
        title=_('DRS API'),  # Title for the doc website
        description=_('RESTful API for DRS')  # Desc for the doc website
    )),
    # Link to api schema
    url(r'^schemas/$', schema_view),
    # Link to demo application
    url(r'^demo/', include('demo.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

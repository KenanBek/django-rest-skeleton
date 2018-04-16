from django.conf.urls import url

from demo import views

urlpatterns = [
    # URLs for demo links
    url(r'^$', views.index, name='demo_index'),
]

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from pitch import urls


urlpatterns = [
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'', include(urls)),
    url(r'^accounts/', include('registration.backends.simple.urls'), name='signup'),
    url(r'^logout/$', views.logout, {"next_page": '/'}),
]

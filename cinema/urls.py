from django.conf.urls import include, url
from django.contrib import admin
from website import urls


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(urls))
]

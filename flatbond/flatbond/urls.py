from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'', include('ui.urls', namespace="ui")),
    url(r'^api/', include('api.urls', namespace="api")),
    url(r'^admin/', admin.site.urls),
]

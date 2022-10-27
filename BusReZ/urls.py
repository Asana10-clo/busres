from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('myapp/', include('myapp.urls')),
    path('users/', include('users.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
]

urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
)

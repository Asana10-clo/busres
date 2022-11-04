from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('myapp.urls')),

    path('dashboard/', user_views.dashboard, name='dashboard'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', user_views.SignUpView.as_view(), name='signup'),

    path("__reload__/", include("django_browser_reload.urls"))
]

urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
)

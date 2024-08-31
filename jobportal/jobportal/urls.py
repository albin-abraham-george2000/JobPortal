from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from errors_handlers.views import BadRequestView,PageNotFoundView,PermissionDeniedView,ServerErrorView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth_users/', include('auth_users.urls', namespace='auth_users')),
    path('', include('core.urls', namespace='core')),
    path("accounts/", include("allauth.urls")),
    path('dashboard/', include('admin_panel.urls', namespace='admin_panel')),
    
]
 # ERROR HANDLERS 
handler400 = BadRequestView.as_view()
handler403 = PermissionDeniedView.as_view()
handler404 = PageNotFoundView.as_view()
handler500 = ServerErrorView.as_view()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
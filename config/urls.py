from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("markdownx/", include("markdownx.urls")),
    path("blog/", include("blog.urls")),
    path("admin/", admin.site.urls),
    # path('accounts/', include('accounts.urls')),
    path("accounts/", include("allauth.urls")),
    path("", include("home_page.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

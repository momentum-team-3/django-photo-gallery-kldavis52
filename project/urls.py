"""project URL Configuration

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
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from api import views as api_views

# api_router = DefaultRouter()
# api_router.register("galleries", viewset=api_views.GalleryViewSet, basename="gallery")

urlpatterns = [
    path("photogalle/", include("photogalle.urls")),
    path("admin/", admin.site.urls),
    path("accounts/", include("registration.backends.simple.urls")),
    path("", RedirectView.as_view(url="photogalle/", permanent=False)),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include("api.urls")),
    # path(
    #     "api/galleries/<int:pk>/image/",
    #     api_views.ImageUploadView.as_view(),
    #     name="image_upload",
    # ),
    # path("api/", include(api_router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

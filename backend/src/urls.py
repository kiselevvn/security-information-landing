from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.i18n import i18n_patterns
from .views import LandingView
from django.views.generic import TemplateView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("content/", include("apps.content.urls")),
    path(
        "privacy/",
        TemplateView.as_view(template_name="service/privacy.html"),
        name="privacy",
    ),
    path(
        "", LandingView.as_view(), name="landing"
    ),
]

urlpatterns = i18n_patterns(
    *urlpatterns,
    prefix_default_language=False,
)


if settings.DEBUG:
    import debug_toolbar

    # pylint: disable=ungrouped-imports
    from django.conf.urls.static import static

    urlpatterns = (
        [
            path("__debug__/", include(debug_toolbar.urls)),
        ]
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        + urlpatterns
    )

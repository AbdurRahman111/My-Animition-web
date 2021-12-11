from django.contrib import admin
from django.urls import path, include
from myapp.views import blog, post_detail, home, add_comment, contact
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("captcha/", include("captcha.urls")),
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("blog/", blog, name="blog"),
    path("blog/<str:title>/", post_detail, name="post_detail"),
    path("blog/<str:title>/add-comment/", add_comment, name="add_comment"),
    path("contact/", contact, name="contact"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

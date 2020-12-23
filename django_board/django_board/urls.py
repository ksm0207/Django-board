from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static, settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("board.urls")),
    path("board/", include("board.urls", namespace="board")),
]
# 이미지 URL 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

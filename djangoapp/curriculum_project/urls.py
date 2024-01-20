from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from curriculum_app import views

urlpatterns = [
    #rota, viem, name
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
]

# to see files of media send by users in development
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

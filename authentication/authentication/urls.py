
from django.contrib import admin

from django.urls import path, include
from authentication.views import AllUser
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('auth/admin/', admin.site.urls),
    path('auth/user-data/', AllUser.as_view()),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

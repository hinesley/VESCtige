from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),

    path('rides/', include('rides.urls')),
    path('api/v1/rides/', include('rides.api.urls')),
]

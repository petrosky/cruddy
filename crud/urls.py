from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('cruddy/', include('cruddy.urls')),
    path('admin/', admin.site.urls),
]

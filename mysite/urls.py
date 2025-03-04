from django.contrib import admin
from django.urls import include, path
#comment
urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
]

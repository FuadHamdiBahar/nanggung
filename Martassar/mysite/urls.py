from django.contrib import admin
from django.urls import path, include

from . views import IndexView, Home

urlpatterns = [
    path('account/', include('account.urls', namespace='account')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('', IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
]

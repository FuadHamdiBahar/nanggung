from django.urls import path

from . views import (
    IndexView,
    ProdukDetailView,
    KeranjangListView,
)

app_name = 'blog'
urlpatterns = [
    path('detail/<pk>', ProdukDetailView.as_view(), name='detail'),
    path('keranjang/<user_id>', KeranjangListView.as_view(), name='keranjang'),
    path('', IndexView.as_view(), name='index')
]

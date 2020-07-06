from django.contrib import admin

# Register your models here.
from . models import Produk, Keranjang


class ProdukAdmin(admin.ModelAdmin):
    readonly_fields = [
        'published',
        'updated',
    ]


admin.site.register(Produk, ProdukAdmin)
admin.site.register(Keranjang)

# import View
from django.views.generic import (
    TemplateView,
    DetailView,
    ListView
)

# import model
from . models import Produk, Keranjang


class KeranjangListView(ListView):
    model = Keranjang
    template_name = 'blog/keranjang.html'
    total_biaya = 0

    def get_queryset(self):
        self.queryset = self.model.objects.filter(
            user_id=self.kwargs['user_id'])

        for i in self.queryset:
            self.total_biaya += int(i.harga_produk) * int(i.jumlah)

        return super().get_queryset()

    def get_context_data(self, **kwargs):
        self.kwargs.update({
            'total_biaya': self.total_biaya
        })
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)


class ProdukDetailView(DetailView):
    model = Produk
    template_name = 'blog/detail.html'
    extra_context = {
        'page_title': 'Detail Produk',
    }

    # def get_context_data(self, **kwargs):
    #     self.kwargs.update(self.extra_context)
    #     kwargs = self.kwargs
    #     return kwargs


class IndexView(TemplateView):
    template_name = 'blog/index.html'
    hasil = Produk.objects.all()
    context_object_name = 'produk'

    def get_context_data(self, **kwargs):
        self.kwargs.update({
            'produk': self.hasil
        })
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)

from mysite import settings
from django.db import models
import os


class Produk(models.Model):
    nama_produk = models.CharField(max_length=255)
    harga = models.PositiveIntegerField()
    nama_toko = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='upload')
    deskripsi = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}. {}'.format(self.id, self.nama_produk)


class User(models.Model):
    nama = models.CharField(max_length=255)

    def __str__(self):
        return '{}. {}'.format(self.id, self.nama_produk)


class Keranjang(models.Model):
    nama_produk = models.CharField(max_length=255)
    harga_produk = models.CharField(max_length=255)
    jumlah = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()
    transaction = models.BooleanField()
    transaction_time = models.DateTimeField(auto_now_add=True)
    success = models.BooleanField()
    success_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}. {}'.format(self.id, self.nama_produk)

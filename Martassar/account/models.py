from django.db import models

# Create your models here.


class Account(models.Model):
    nama = models.CharField(max_length=255)
    gender_choices = [
        ('0', 'Laki-Laki'),
        ('1', 'Perempuan'),
    ]
    gender = models.CharField(max_length=20, choices=gender_choices)
    umur = models.PositiveIntegerField()
    alamat = models.CharField(max_length=255)
    password1 = models.CharField(max_length=255)
    password2 = models.CharField(max_length=255)

    def __str__(self):
        return "{}. {}". format(self.id, self. nama)

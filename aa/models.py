from django.contrib.auth.models import User
from django.db import models


class Raions(models.Model):
    raion = models.CharField(max_length=20)

    def __str__(self):
        return self.raion


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.ForeignKey(
        'Addresses',
        on_delete=models.CASCADE,
        related_name='back_note',
    )

    def __str__(self):
        return self.text


class Addresses(models.Model):
    num = models.IntegerField()
    address = models.CharField(max_length=255)
    raion = (models.ForeignKey(
        'Raions',
        on_delete=models.CASCADE,
        related_name='back_addresses')
    )

    def __str__(self):
        return self.address


class Types(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.type


class Devices(models.Model):
    ip = models.GenericIPAddressField()
    mask = models.CharField(max_length=15)
    gw = models.GenericIPAddressField()
    address = (models.ForeignKey(
        'Addresses',
        on_delete=models.CASCADE,
        related_name='back_device')
    )
    type = (models.ForeignKey(
        'Types',
        on_delete=models.CASCADE,
        related_name='back_type')
    )

    def __str__(self):
        return self.ip

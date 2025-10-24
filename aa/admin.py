from django.contrib import admin

from .models import Raions, Addresses, Devices, Types, Note


@admin.register(Raions)
class RaionAdmin(admin.ModelAdmin):
    list_display = ('id', 'raion')


@admin.register(Addresses)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'num', 'address')


@admin.register(Devices)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'ip', 'mask', 'gw', 'type')


@admin.register(Types)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type')


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'text', 'created_at')

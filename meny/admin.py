from django.contrib import admin
from .models import Burgare, Nyhet, Erbjudande
from .models import Banner

class BurgareAdmin(admin.ModelAdmin):
    list_display = ('namn', 'kategori', 'pris', 'popular')
    list_filter = ('kategori', 'popular')

admin.site.register(Burgare, BurgareAdmin)

class BannerAdmin(admin.ModelAdmin):
    list_display = ('text', 'aktiv', 'farg')

admin.site.register(Banner)

class ErbjudandeAdmin(admin.ModelAdmin):
    list_display = ('titel', 'publicerad')

admin.site.register(Erbjudande, ErbjudandeAdmin)

class NyhetAdmin(admin.ModelAdmin):
    list_display = ('titel', 'publicerad')

admin.site.register(Nyhet, NyhetAdmin)
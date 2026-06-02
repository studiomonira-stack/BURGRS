from django.contrib import admin
from .models import Burgare, Nyhet, Erbjudande

class BurgareAdmin(admin.ModelAdmin):
    list_display = ('namn', 'kategori', 'pris', 'popular')
    list_filter = ('kategori', 'popular')

admin.site.register(Burgare, BurgareAdmin)

class ErbjudandeAdmin(admin.ModelAdmin):
    list_display = ('titel', 'publicerad')

admin.site.register(Erbjudande, ErbjudandeAdmin)

class NyhetAdmin(admin.ModelAdmin):
    list_display = ('titel', 'publicerad')

admin.site.register(Nyhet, NyhetAdmin)
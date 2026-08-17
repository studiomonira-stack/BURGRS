from django.contrib import admin
from .models import Burgare, Nyhet, Erbjudande, Banner
from .models import PollAlternativ

class BurgareAdmin(admin.ModelAdmin):
    list_display = ('ordning', 'namn', 'kategori', 'pris', 'popular')
    list_display_links = ('namn',)
    list_filter = ('kategori', 'popular')
    list_editable = ('ordning',)

admin.site.register(Burgare, BurgareAdmin)

class BannerAdmin(admin.ModelAdmin):
    list_display = ('text', 'typ', 'aktiv')
    list_filter = ('typ', 'aktiv')

admin.site.register(Banner, BannerAdmin)

class ErbjudandeAdmin(admin.ModelAdmin):
    list_display = ('titel', 'publicerad')
    list_filter = ('publicerad',)

admin.site.register(Erbjudande, ErbjudandeAdmin)

class NyhetAdmin(admin.ModelAdmin):
    list_display = ('titel', 'publicerad')

admin.site.register(Nyhet, NyhetAdmin)

@admin.register(PollAlternativ)
class PollAlternativAdmin(admin.ModelAdmin):
    list_display = ('namn', 'aktiv', 'ordning')
    list_editable = ('aktiv', 'ordning')
from .models import Banner

def banners(request):
    return {'banners': Banner.objects.filter(aktiv=True)}
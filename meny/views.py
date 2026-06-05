from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Burgare, Nyhet, Erbjudande, Rost, AnvantErbjudande

def hem(request):
    burgare = Burgare.objects.all().order_by('ordning', '-popular', '-skapad')
    return render(request, 'meny/hem.html', {'burgare': burgare})

from .models import Burgare, Nyhet, Erbjudande, Rost

def youmatter(request):
    google_review_url = "https://tinyurl.com/burgrssarajevo"
    
    # Räkna röster
    rost_truffle = Rost.objects.filter(val='truffle').count()
    rost_sambal = Rost.objects.filter(val='sambal').count()
    rost_balkan = Rost.objects.filter(val='balkan').count()
    total_rost = rost_truffle + rost_sambal + rost_balkan
    
    # Har användaren redan röstat?
    har_rostat = False
    if request.user.is_authenticated:
        har_rostat = Rost.objects.filter(user=request.user).exists()
    
    return render(request, 'meny/youmatter.html', {
        'google_review_url': google_review_url,
        'rost_truffle': rost_truffle,
        'rost_sambal': rost_sambal,
        'rost_balkan': rost_balkan,
        'total_rost': total_rost,
        'har_rostat': har_rostat,
    })


def rosta(request):
    if request.method == 'POST' and request.user.is_authenticated:
        val = request.POST.get('val')
        if val and not Rost.objects.filter(user=request.user).exists():
            Rost.objects.create(user=request.user, val=val)
    return redirect('youmatter')

def nyheter(request):
    alla_nyheter = Nyhet.objects.all().order_by('-publicerad')
    return render(request, 'meny/news.html', {'nyheter': alla_nyheter})

@login_required
def erbjudanden(request):
    alla = Erbjudande.objects.all().order_by('-publicerad')
    anvanda = AnvantErbjudande.objects.filter(user=request.user).values_list('erbjudande_id', flat=True)
    return render(request, 'meny/offers.html', {
        'erbjudanden': alla,
        'anvanda': anvanda,
    })

@login_required
def anvand_erbjudande(request, erbjudande_id):
    erbjudande = get_object_or_404(Erbjudande, id=erbjudande_id)
    if not AnvantErbjudande.objects.filter(user=request.user, erbjudande=erbjudande).exists():
        AnvantErbjudande.objects.create(user=request.user, erbjudande=erbjudande)
    return redirect('erbjudanden')

def dashboard(request):
    burgare = Burgare.objects.filter(popular=True).first()
    senaste_nyhet = Nyhet.objects.order_by('-publicerad').first()
    return render(request, 'meny/dashboard.html', {
        'featured': burgare,
        'senaste_nyhet': senaste_nyhet,
    })
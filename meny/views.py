from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Burgare, Nyhet, Erbjudande, PollAlternativ, Rost, AnvantErbjudande

def hem(request):
    burgare = Burgare.objects.all().order_by('ordning', '-popular', '-skapad')
    return render(request, 'meny/hem.html', {'burgare': burgare})

def youmatter(request):
    google_review_url = "https://tinyurl.com/burgrssarajevo"
    
    # Hämta alla aktiva poll-alternativ
    poll_alternativ = PollAlternativ.objects.filter(aktiv=True).order_by('ordning')
    
    # Räkna röster per alternativ
    rost_resultat = []
    for alt in poll_alternativ:
        antal = Rost.objects.filter(val=alt.namn).count()
        rost_resultat.append({'namn': alt.namn, 'antal': antal})
    
    total_rost = sum(r['antal'] for r in rost_resultat)
    
    # Har användaren redan röstat?
    har_rostat = False
    if request.user.is_authenticated:
        har_rostat = Rost.objects.filter(user=request.user).exists()
    
    return render(request, 'meny/youmatter.html', {
        'google_review_url': google_review_url,
        'poll_alternativ': poll_alternativ,
        'rost_resultat': rost_resultat,
        'total_rost': total_rost,
        'har_rostat': har_rostat,
    })


def rosta(request):
    if request.method == 'POST' and request.user.is_authenticated:
        alt_id = request.POST.get('val')
        if alt_id and not Rost.objects.filter(user=request.user).exists():
            alternativ = get_object_or_404(PollAlternativ, id=alt_id, aktiv=True)
            Rost.objects.create(user=request.user, val=alternativ.namn)
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

def privacy(request):
    return render(request, 'meny/privacy.html')

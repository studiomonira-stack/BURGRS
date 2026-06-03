from django.db import models
from django.contrib.auth.models import User


class Burgare(models.Model):
    KATEGORIER = [
        ('burgers', 'Burgers'),
        ('sides', 'Sides'),
        ('dips', 'Dips'),
    ]

    namn = models.CharField(max_length=100)
    beskrivning = models.TextField()
    pris = models.DecimalField(max_digits=6, decimal_places=0)
    bild_url = models.URLField(max_length=500)
    kategori = models.CharField(max_length=20, choices=KATEGORIER, default='burgers')
    popular = models.BooleanField(default=False)
    skapad = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.namn} ({self.get_kategori_display()})"


class Nyhet(models.Model):
    titel = models.CharField(max_length=200)
    text = models.TextField()
    bild_url = models.URLField(max_length=500, blank=True)
    publicerad = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titel


class Erbjudande(models.Model):
    titel = models.CharField(max_length=200)
    text = models.TextField()
    kod = models.CharField(max_length=50, blank=True)
    bild_url = models.URLField(max_length=500, blank=True)
    publicerad = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titel


class Rost(models.Model):
    BURGARE = [
        ('truffle', 'The Truffle Beast'),
        ('sambal', 'Spicy Sambal Crunch'),
        ('balkan', 'Balkan Breakfast Burger'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    val = models.CharField(max_length=20, choices=BURGARE)
    skapad = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [('user',)]

    def __str__(self):
        return f"{self.user.username} - {self.val}"


class AnvantErbjudande(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    erbjudande = models.ForeignKey(Erbjudande, on_delete=models.CASCADE)
    anvant_datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [('user', 'erbjudande')]

    def __str__(self):
        return f"{self.user.username} - {self.erbjudande.titel}"

    class Banner(models.Model):
        text = models.CharField(max_length=200)
        aktiv = models.BooleanField(default=True)
        farg = models.CharField(max_length=7, default='#F5A623')  # Gul som standard
        text_farg = models.CharField(max_length=7, default='#0B0B0B')  # Svart text
        skapad = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]
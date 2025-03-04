from django.shortcuts import render, get_object_or_404
from .models import Produit, Categorie, Client, Vente, Paiement, Recu
from django.contrib import messages

# Vue pour la page d'accueil
def home(request):
    home = 'active'  # Pour activer le bouton Accueil dans la barre de navigation
    return render(request, 'BoutiqueApp/home.html')

# Vue pour afficher la liste des produits
def produits(request):
    produits = Produit.objects.all().order_by('-id')  # Tri par ID décroissant
    return render(request, 'BoutiqueApp/produits.html', {'produits': produits})

# Vue pour afficher la liste des catégories
def categories(request):
    categories = Categorie.objects.all()
    return render(request, 'BoutiqueApp/categories.html', {'categories': categories})

# Vue pour afficher la liste des clients
def clients(request):
    clients = Client.objects.all()
    return render(request, 'BoutiqueApp/clients.html', {'clients': clients})

# Vue pour afficher la liste des ventes
def ventes(request):
    ventes = Vente.objects.all().order_by('-date')  # Trier par date de vente
    return render(request, 'BoutiqueApp/ventes.html', {'ventes': ventes})

# Vue pour afficher la liste des paiements
def paiements(request):
    paiements = Paiement.objects.all().order_by('-date_paiement')
    return render(request, 'BoutiqueApp/paiements.html', {'paiements': paiements})

# Vue pour afficher la liste des reçus
def recus(request):
    recus = Recu.objects.all().order_by('-date_creation')

    # Ajouter un message si un client a un reçu sans paiement
    recus_non_payes = Recu.objects.filter(stat_paiement="Non payé").count()
    if recus_non_payes > 0:
        messages.warning(request, f"Il y a {recus_non_payes} reçu(s) non payé(s).")

    return render(request, 'Boutique/recus.html', {'recus': recus})
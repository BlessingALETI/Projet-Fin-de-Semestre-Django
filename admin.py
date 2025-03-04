from django.contrib import admin
from .models import Utilisateur, Categorie, Produit, Client, Vente, Paiement, Recu

class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix', 'categorie')  # Assurez-vous que ces champs existent dans le modèle
    search_fields = ('nom',)
    list_filter = ('categorie',)

admin.site.register(Utilisateur)
admin.site.register(Categorie)
admin.site.register(Produit, ProduitAdmin)
admin.site.register(Client)
admin.site.register(Vente)
admin.site.register(Paiement)
admin.site.register(Recu)
from django.db import models

# Modèle pour les utilisateurs
class Utilisateur(models.Model):
    nom = models.CharField(max_length=50)
    role = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nom} ({self.role})"

# Modèle pour les catégories de produits
class Categorie(models.Model):
    nom = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nom

# Modèle pour les produits
class Produit(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)  # Description optionnelle
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    quantite = models.PositiveIntegerField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name="produits")

    def __str__(self):
        return f"{self.nom} ({self.prix} Fcfa)"

# Modèle pour les clients
class Client(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    numero = models.CharField(max_length=15)
    adresse = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nom} - {self.email}"

# Modèle pour les ventes
class Vente(models.Model):
    date = models.DateField(auto_now_add=True)
    montant_total = models.DecimalField(max_digits=10, decimal_places=2)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="ventes")

    def __str__(self):
        return f"Vente #{self.id} - {self.client.nom} - {self.date}"

# Modèle pour les paiements
class Paiement(models.Model):
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    mode_paiement = models.CharField(max_length=50)
    date_paiement = models.DateField(auto_now_add=True)
    vente = models.ForeignKey(Vente, on_delete=models.CASCADE, related_name="paiements")

    def __str__(self):
        return f"Paiement de {self.montant} Fcfa via {self.mode_paiement}"

# Modèle pour les reçus
class Recu(models.Model):
    date_creation = models.DateTimeField(auto_now_add=True)
    date = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="recus")
    vente = models.ForeignKey(Vente, on_delete=models.CASCADE, related_name="recus")
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self):
        return f"Reçu #{self.id} - {self.client.nom} - {self.montant} Fcfa"

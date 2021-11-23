from django.db import models

class Client(models.Model):
    nom = models.CharField(db_column="nom", max_length=100)
    prenom = models.CharField(db_column="prenom", max_length=100)
    dateNais = models.DateField(db_column="dateNais")
    telephone = models.CharField(db_column="telephone", max_length=100)
    adresse = models.CharField(db_column="adresse", max_length=100)
    sexe = models.CharField(db_column="sexe", max_length=100)
    
    class Meta:
        db_table = 'tbClient'
        
class Produit(models.Model):
    designation = models.CharField(db_column="designation", max_length=100)
    prix = models.FloatField(db_column="prix")
    quantite = models.IntegerField(db_column="quantite")
    
    class Meta:
        db_table = 'tbProduit'
        
class Fournisseur(models.Model):
    nom = models.CharField(db_column="nom", max_length=100)
    mail = models.CharField(db_column="mail", max_length=100)
    telephone = models.CharField(db_column="telephone", max_length=100)
    secteur = models.CharField(db_column="secteur", max_length=100)
    
    class Meta:
        db_table = 'tbFournisseur'

class Commande(models.Model):
    dateCommande = models.DateTimeField(db_column="dateCommande", auto_now=True)
    livraison = models.CharField(db_column="livraison", max_length=200)
    refClient = models.ForeignKey(Client, db_column="refClient", on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'tbCommande'

class DetailCommande(models.Model):
    qte = models.FloatField(db_column="qte")
    montant = models.FloatField(db_column="montant")
    refProduit = models.ForeignKey(Produit, db_column="refProduit", on_delete=models.CASCADE)
    refCommande = models.ForeignKey(Commande, db_column="refCommande", on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'tbDetailCommande'

class Paiement(models.Model):
    datePaiement = models.DateTimeField(db_column="datePaiement", auto_now=True)
    montantPaye = models.FloatField(db_column="montantPaye")
    refCommande = models.ForeignKey(Commande, db_column="refCommande", on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'tbPaiement'



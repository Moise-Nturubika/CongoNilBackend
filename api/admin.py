from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Client)
admin.site.register(Fournisseur)
admin.site.register(Commande)
admin.site.register(DetailCommande)
admin.site.register(Paiement)
admin.site.register(Produit)
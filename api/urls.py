from django.urls import path
from . import views

urlpatterns = [
    #All path related to client
    path('client/show/all', views.getAllClient),
    # path('client/show/<int:pk>', views.getDeviceById),
    path('client/save', views.saveClient),
    path('client/update/<int:pk>', views.updateClient),
    path('client/delete', views.deleteClient),
    
    #All path related to product
    path('product/show/all', views.getAllProduct),
    # path('client/show/<int:pk>', views.getDeviceById),
    path('product/save', views.saveProduct),
    path('product/delete', views.deleteProduit),
    # path('product/update/<int:pk>', views.upda),
    # path('client/delete/<int:pk>', views.deleteClient),
    
    #All path related to fournisseur
    path('fournisseur/show/all', views.getAllFournisseur),
    path('fournisseur/save', views.saveFournisseur),
    path('fournisseur/delete', views.deleteFournisseur),
    # path('client/show/<int:pk>', views.getDeviceById),
    # path('client/save', views.saveClient),
    # path('client/update/<int:pk>', views.updateClient),
    # path('client/delete/<int:pk>', views.deleteClient),
    
    
    path('command/show/all', views.getAllCommands),
    path('command/save', views.saveCommande),
    path('command/delete', views.deleteCommand),
    
    path('approv/save', views.saveApprovis),
]

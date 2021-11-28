from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from django.db.models import Sum
from .models import *
from .serializers import *

#########################
#        CLIENT        #
########################
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getAllClient(request):
    clients = Client.objects.all()
    cl_serialiser = ClientSerializer(clients, many= True)
    return JsonResponse(cl_serialiser.data, safe=False)

@api_view(['POST'])
def saveClient(request):
    status = { 'status': False }
    cl_serialiser = ClientSerializer(data=request.data)
    if cl_serialiser.is_valid():
        client = cl_serialiser.save()
        if client:
            status = { 'status': True, 'message': 'Client saved successfully'}
        else:
            status = { 'status': False, 'message': 'Client not saved'}
    else:
        print(cl_serialiser.errors)
        status = { 'status': False, 'message': 'Client data are not valid'}
    return JsonResponse(status)

@api_view(['POST'])
def updateClient(request):
    status = { 'status': False }
    return JsonResponse(status)

# @api_view(['DELETE'])
# def deleteClient(request, pk):
#     client = Client.objects.get(pk=pk)
#     if client:
#         client.delete()
#         status = {'status': True, 'message': 'Client deleted succefully'}
#     else:
#         status = {'status': False, 'message': 'Client does not exists'}
#     return JsonResponse(status)


#########################
#        PRODUIT        #
#########################

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getAllProduct(request):
    prods = Produit.objects.all()
    p_serialiser = ProduitSerializer(prods, many= True)
    return JsonResponse(p_serialiser.data, safe=False)

@api_view(['POST'])
def saveProduct(request):
    status = { 'status': False }
    p_serialiser = ProduitSerializer(data=request.data)
    if p_serialiser.is_valid():
        prod = p_serialiser.save()
        if prod:
            status = { 'status': True, 'message': 'Product saved successfully'}
        else:
            status = { 'status': False, 'message': 'Product not saved'}
    else:
        status = { 'status': False, 'message': 'Product data are not valid'}
    return JsonResponse(status)

@api_view(['POST'])
def updateProduct(request):
    status = { 'status': False }
    return JsonResponse(status)

@api_view(['DELETE'])
def deleteProduct(request, pk):
    prod = Produit.objects.get(pk=pk)
    if prod:
        prod.delete()
        status = {'status': True, 'message': 'Product deleted succefully'}
    else:
        status = {'status': False, 'message': 'Product does not exists'}
    return JsonResponse(status)


#########################
#     FOURNINSSEUR      #
#########################

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getAllFournisseur(request):
    fss = Fournisseur.objects.all()
    f_serialiser = FournisseurSerializer(fss, many= True)
    return JsonResponse(f_serialiser.data, safe=False)

@api_view(['POST'])
def saveFournisseur(request):
    status = { 'status': False }
    f_serialiser = FournisseurSerializer(data=request.data)
    if f_serialiser.is_valid():
        fss = f_serialiser.save()
        if fss:
            status = { 'status': True, 'message': 'Fournisseur saved successfully'}
        else:
            status = { 'status': False, 'message': 'Fournisseur not saved'}
    else:
        status = { 'status': False, 'message': 'Fournisseur data are not valid'}
    return JsonResponse(status)

@api_view(['POST'])
def updateFss(request):
    status = { 'status': False }
    return JsonResponse(status)

@api_view(['DELETE'])
def deleteFournisseur(request, pk):
    fss = Fournisseur.objects.get(pk=pk)
    if fss:
        fss.delete()
        status = {'status': True, 'message': 'Fournisseur deleted succefully'}
    else:
        status = {'status': False, 'message': 'Fournisseur does not exists'}
    return JsonResponse(status)

@api_view(['GET'])
def getAllCommands(request):
    data = []
    cmds = Commande.objects.all()
    for cmd in cmds:
        detailsCmd = []
        dtlCmds = DetailCommande.objects.filter(refCommande=cmd.id)
        sumMontant = DetailCommande.objects.filter(refCommande=cmd.id).aggregate(Sum('montant'))
        for dtl in dtlCmds:
            detailsCmd.append({
                'id': dtl.id,
                'qte': dtl.qte,
                'montant': dtl.montant,
                'produit': {
                    'id': dtl.refProduit.id,
                    'designation': dtl.refProduit.designation,
                    'prix': dtl.refProduit.prix
                }
            })
        data.append(
            {
                'id': cmd.id,
                'dateCommande': cmd.dateCommande,
                'livraison': cmd.livraison,
                'total': sumMontant['montant__sum'],
                'client': {
                    'id': cmd.refClient.id,
                    'nom': cmd.refClient.nom,
                    'prenom': cmd.refClient.prenom,
                    'telephone': cmd.refClient.telephone
                },
                'countProduit': len(dtlCmds),
                'details': detailsCmd
            }
        )
    return JsonResponse(data, safe=False)

@api_view(['POST'])
def saveCommande(request):
    status = { 'status': False }
    cmd_serialiser = CommandeSerializer(data=request.data.get('command'))
    dtlCmds = request.data.get('details')
    if cmd_serialiser.is_valid():
        cmd = cmd_serialiser.save()
        try:
            if cmd:
                for data in dtlCmds:
                    dtl = {
                        'qte': data['qte'],
                        'montant': data['montant'],
                        'refCommande': cmd.id,
                        'refProduit': data['refProduit']
                    }
                    dtl_serializer = DetailCmdSerializer(data=dtl)
                    dtl_serializer.is_valid()
                    dtlRes = dtl_serializer.save()
                status = { 'status': True, 'message': 'Command saved successfully'}
            else:
                status = { 'status': False, 'message': 'Command not saved'}
        except Exception as exc:
            cmd.delete()
            print('Error occured')
    else:
        status = { 'status': False, 'message': 'Command data are not valid'}
    return JsonResponse(status)

@api_view(['POST'])
def deleteCommand(request):
    status = {'status': False}
    try:
        idCmd = request.data.get('id')
        cmd = Commande.objects.get(pk=idCmd)
        cmd.delete()
        status = { 'status': True, 'message': 'Command deleted successfully' }
    except Exception as exc:
        status = { 'status': False, 'message': 'An exception thrown' }
        print(f"Error occured : {exc.message}")
    return JsonResponse(status)
    
@api_view(['POST'])
def deleteClient(request):
    status = {'status': False}
    try:
        idClient = request.data.get('id')
        client = Client.objects.get(pk=idClient)
        client.delete()
        status = { 'status': True, 'message': 'Client deleted successfully' }
    except Exception as exc:
        status = { 'status': False, 'message': 'An exception thrown' }
        print(f"Error occured : {exc.message}")
    return JsonResponse(status)

@api_view(['POST'])
def deleteProduit(request):
    status = {'status': False}
    try:
        idProd = request.data.get('id')
        prod = Produit.objects.get(pk=idProd)
        prod.delete()
        status = { 'status': True, 'message': 'Produit deleted successfully' }
    except Exception as exc:
        status = { 'status': False, 'message': 'An exception thrown' }
        print(f"Error occured : {exc.message}")
    return JsonResponse(status)

@api_view(['POST'])
def deleteFournisseur(request):
    status = {'status': False}
    try:
        idFss = request.data.get('id')
        fss = Fournisseur.objects.get(pk=idFss)
        fss.delete()
        status = { 'status': True, 'message': 'Fournisseur deleted successfully' }
    except Exception as exc:
        status = { 'status': False, 'message': 'An exception thrown' }
        print(f"Error occured : {exc.message}")
    return JsonResponse(status)

@api_view(['POST'])
def saveApprovis(request):
    status = { 'status': False }
    approvSerializer = ApprovSerializer(data=request.data)
    if approvSerializer.is_valid():
        approv = approvSerializer.save()
        try:
            if approv:
                prod = Produit.objects.get(pk=approv.refProduit.id)
                oldQte = prod.quantite
                prod.quantite = oldQte + approv.quantite
                prod.save()
                status = { 'status': True, 'message': 'Approv saved successfully'}
            else:
                status = { 'status': False, 'message': 'Approv not saved'}
        except Exception as exc:
            approv.delete()
            print(f'Error occured ===> {exc}')
    else:
        status = { 'status': False, 'message': 'Approv data are not valid'}
    return JsonResponse(status)

@api_view(['GET'])
def getAllApprov(request):
    data = []
    approvs = Approvisionnement.objects.all()
    for appr in approvs:
        data.append(
            {
                'id': appr.id,
                'dateApprov': appr.dateApprov,
                'quantite': appr.quantite,
                'fournisseur': {
                    'id': appr.refFss.id,
                    'nom': appr.refFss.nom,
                    'mail': appr.refFss.mail,
                    'secteur': appr.refFss.secteur
                },
                'produit': {
                    'id': appr.refProduit.id,
                    'designation': appr.refProduit.designation,
                    'prix': appr.refProduit.prix,
                    'quantite': appr.refProduit.quantite
                }
            }
        )
    return JsonResponse(data, safe=False)
# Generated by Django 3.1.5 on 2021-11-09 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(db_column='nom', max_length=100)),
                ('prenom', models.CharField(db_column='prenom', max_length=100)),
                ('dateNais', models.DateField(db_column='dateNais')),
                ('telephone', models.CharField(db_column='telephone', max_length=100)),
                ('sexe', models.CharField(db_column='sexe', max_length=100)),
            ],
            options={
                'db_table': 'tbClient',
            },
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCommande', models.DateTimeField(auto_now=True, db_column='dateCommande')),
                ('livraison', models.CharField(db_column='livraison', max_length=200)),
                ('refClient', models.ForeignKey(db_column='refClient', on_delete=django.db.models.deletion.CASCADE, to='api.client')),
            ],
            options={
                'db_table': 'tbCommande',
            },
        ),
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(db_column='nom', max_length=100)),
                ('mail', models.CharField(db_column='mail', max_length=100)),
                ('telephone', models.CharField(db_column='telephone', max_length=100)),
                ('secteur', models.CharField(db_column='secteur', max_length=100)),
            ],
            options={
                'db_table': 'tbFournisseur',
            },
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(db_column='designation', max_length=100)),
                ('prix', models.FloatField(db_column='prix')),
            ],
            options={
                'db_table': 'tbProduit',
            },
        ),
        migrations.CreateModel(
            name='Paiement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datePaiement', models.DateTimeField(auto_now=True, db_column='datePaiement')),
                ('montantPaye', models.FloatField(db_column='montantPaye')),
                ('refCommande', models.ForeignKey(db_column='refCommande', on_delete=django.db.models.deletion.CASCADE, to='api.commande')),
            ],
            options={
                'db_table': 'tbPaiement',
            },
        ),
        migrations.CreateModel(
            name='DetailCommande',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qte', models.FloatField(db_column='qte')),
                ('montant', models.FloatField(db_column='montant')),
                ('refCommande', models.ForeignKey(db_column='refCommande', on_delete=django.db.models.deletion.CASCADE, to='api.commande')),
                ('refProduit', models.ForeignKey(db_column='refProduit', on_delete=django.db.models.deletion.CASCADE, to='api.produit')),
            ],
            options={
                'db_table': 'tbDetailCommande',
            },
        ),
    ]

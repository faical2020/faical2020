from django.db import models

# Create your models here.
class Preprod(models.Model):
    date_mise_a_jour = models.DateField(verbose_name="date de mise à jour",auto_now=False)
    machine_name = models.CharField(max_length=64)
    pack_id = models.IntegerField(unique=True)
    odc = models.IntegerField()
    quantite = models.IntegerField()
    carte_perso_ok = models.IntegerField()
    rejet_machine = models.IntegerField()
    retoure_stock = models.IntegerField()
    autres = models.IntegerField(default=0)
    date_de_creation =  models.DateField(verbose_name="date de 1er creation",auto_now_add=True)
    commentaire = models.CharField(max_length=1000, blank = True)
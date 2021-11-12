from django.db import models

# Create your models here.
class Preprod(models.Model):
    MachineName  = [
        ('MAR1', 'MAR1'),
        ('MAR2', 'MAR2'),
    ]

    date_mise_a_jour = models.DateField(verbose_name="date de mise à jour",auto_now=False)
    
    machine = models.CharField(choices=MachineName, max_length=4,default='MAR1')
    pack_id = models.IntegerField(verbose_name="ID du Pck",unique=True)
    odc = models.IntegerField(verbose_name="N° ODC",)
    quantite = models.IntegerField(verbose_name="Quantité",)
    carte_perso_ok = models.IntegerField(verbose_name="carte personalisé ok",)
    rejet_machine = models.IntegerField(verbose_name="rejets de la machine",)
    retoure_stock = models.IntegerField(verbose_name="Retour au stock",)
    autres = models.IntegerField(verbose_name="autres problèmes",default=0)
    date_de_creation =  models.DateField(verbose_name="date de 1er creation",auto_now_add=True)
    commentaire = models.CharField(max_length=1000, blank = True)

    def __str__(self):
        return " date_mise_a_jour= %s machine_name= %s pack_id= %s odc=%s quantite=%s carte_perso_ok=%s" % (self.date_mise_a_jour,
        self.machine_name , self.pack_id ,self.odc ,self.quantite ,self.carte_perso_ok )

from django.db import models

from .preprod import Preprod

# Create your models here.
class Qcontrol(models.Model):
    preprod= models.OneToOneField(Preprod, on_delete=models.CASCADE, related_name="Qprod"  )
    date_mise_a_jour = models.DateField(verbose_name="date de mise à jour",auto_now=False,null=True)
    carte_ok = models.IntegerField(null=True)
    rejet = models.IntegerField(null=True)
    retoure_stock = models.IntegerField(null=True)
    autres = models.IntegerField(default=0)
    commentaire = models.CharField(max_length=1000, blank = True)

    def __str__(self):
        return " date_mise_a_jour= %s carte_ok= %s rejet= %s retoure_stock=%s autres=%s commentaire=%s" % (self.date_mise_a_jour,
        self.carte_ok , self.rejet ,self.retoure_stock ,self.autres ,self.commentaire )
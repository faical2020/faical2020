from django.db import models

from .preprod import Preprod
from .qcontrol import Qcontrol

# Create your models here.
class Rejprod(models.Model):
    date_mise_a_jour = models.DateField(verbose_name="date de mise à jour",auto_now=False)
    quantite = models.IntegerField()
    carte_ok = models.IntegerField()
    rejet = models.IntegerField()
    retoure_stock = models.IntegerField()
    autres = models.IntegerField(default=0)
    commentaire = models.CharField(max_length=1000, blank = True)
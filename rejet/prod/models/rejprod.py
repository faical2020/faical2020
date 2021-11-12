from django.db import models

from .preprod import Preprod
from .qcontrol import Qcontrol

# Create your models here.
class Rejprod(models.Model):
    qcontrol= models.OneToOneField(Qcontrol, on_delete=models.CASCADE, related_name="Rctrl"  )
    date_mise_a_jour = models.DateField(verbose_name="date de mise à jour",auto_now=False)
    
    nd = models.IntegerField(null=True)
    
    autres = models.IntegerField(default=0)
    commentaire = models.CharField(max_length=1000, blank = True)
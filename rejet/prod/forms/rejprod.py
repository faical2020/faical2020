from django.forms import ModelForm, fields

from prod.models.preprod import Preprod
from prod.models.qcontrol import Qcontrol
from prod.models.rejprod import Rejprod

class RejprodForm(ModelForm):
    class Meta:
        model = Rejprod
        fields = ("date_mise_a_jour","quantite","carte_ok","rejet","retoure_stock","autres","commentaire")

from django.forms import ModelForm, fields

from prod.models.preprod import Preprod
from prod.models.qcontrol import Qcontrol

class QcontrolForm(ModelForm):
    class Meta:
        model = Qcontrol
        fields = ("date_mise_a_jour","carte_ok","rejet","retoure_stock","autres","commentaire")

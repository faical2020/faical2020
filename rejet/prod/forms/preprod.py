from django.forms import ModelForm, fields

from prod.models.preprod import Preprod

class PreprodForm(ModelForm):
    class Meta:
        model = Preprod
        fields = ("date_mise_a_jour","machine_name","pack_id","odc"
        ,"quantite","carte_perso_ok","rejet_machine","retoure_stock"
        ,"commentaire")
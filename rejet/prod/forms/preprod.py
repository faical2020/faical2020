from django.forms import ModelForm, fields, Form, DateField, IntegerField,CharField, TextInput

from prod.models.preprod import Preprod

class PreprodForm(ModelForm):
    class Meta:
        model = Preprod
        fields = ("date_mise_a_jour","machine_name","pack_id","odc"
        ,"quantite","carte_perso_ok","rejet_machine","retoure_stock"
        ,"autres","commentaire")

class PreprodSearchForm(Form):
    
    packid = CharField(required=False, widget= TextInput(attrs={'placeholder': 'pack_id'}) )
    odc = CharField(required=False, widget= TextInput(attrs={'placeholder': 'odc'}) )
    quantite = CharField(required=False, widget= TextInput(attrs={'placeholder': 'quantité'}) )
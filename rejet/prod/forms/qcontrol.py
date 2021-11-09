from django.forms import ModelForm, fields, Form, DateField, IntegerField,CharField, TextInput

from prod.models.preprod import Preprod
from prod.models.qcontrol import Qcontrol

class QcontrolForm(ModelForm):
    class Meta:
        model = Qcontrol
        fields = ("date_mise_a_jour","carte_ok","rejet","retoure_stock","autres","commentaire")
        widgets={
            'date_mise_a_jour': TextInput(attrs={'class':'form-control',}),
            'carte_ok': TextInput(attrs={'class':'form-control',}),
            'rejet': TextInput(attrs={'class':'form-control',}),
            'retoure_stock': TextInput(attrs={'class':'form-control',}),
            'autres': TextInput(attrs={'class':'form-control',}),
            'commentaire': TextInput(attrs={'class':'form-control',}),
        }

class QcontrolSearchForm(Form):
    
    packid = CharField(required=False, widget= TextInput(attrs={'placeholder': 'pack_id'}) )
    odc = CharField(required=False, widget= TextInput(attrs={'placeholder': 'odc'}) )
    quantite = CharField(required=False, widget= TextInput(attrs={'placeholder': 'quantité'}) )
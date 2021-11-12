from django.forms import ModelForm, fields, Form, DateField, IntegerField,CharField, TextInput, DateInput , Textarea

from prod.models.preprod import Preprod
from prod.models.qcontrol import Qcontrol
from prod.models.rejprod import Rejprod

class RejprodForm(ModelForm):
    class Meta:
        model = Rejprod
        fields = ("date_mise_a_jour","nd","autres","commentaire")
        widgets={
            'date_mise_a_jour': DateInput(attrs={'class':'form-control',}),
            
            'nd': TextInput(attrs={'class':'form-control',}),
            
            'autres': TextInput(attrs={'class':'form-control',}),
            'commentaire': Textarea(attrs={'rows':'5','class':'form-control',}),
        }

class RejprodSearchForm(Form):
    
    packid = CharField(required=False, widget= TextInput(attrs={'placeholder': 'pack_id'}) )
    odc = CharField(required=False, widget= TextInput(attrs={'placeholder': 'odc'}) )
    quantite = CharField(required=False, widget= TextInput(attrs={'placeholder': 'quantité'}) )
    


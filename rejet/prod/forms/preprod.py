from django.forms import ModelForm, fields, Form, DateField, IntegerField,CharField, TextInput, DateInput , Textarea

from prod.models.preprod import Preprod

class PreprodForm(ModelForm):
    class Meta:
        model = Preprod
        fields = ("date_mise_a_jour","machine","pack_id","odc"
        ,"quantite","carte_perso_ok","rejet_machine","retoure_stock"
        ,"autres","commentaire")
        widgets={
            'date_mise_a_jour': DateInput(attrs={'class':'form-control',}),
            
            'pack_id': TextInput(attrs={'class':'form-control',}),
            'odc': TextInput(attrs={'class':'form-control',}),
            'quantite': TextInput(attrs={'class':'form-control',}),
            'carte_perso_ok': TextInput(attrs={'class':'form-control',}),
            'rejet_machine': TextInput(attrs={'class':'form-control',}),
            'retoure_stock': TextInput(attrs={'class':'form-control',}),
            'autres': TextInput(attrs={'class':'form-control',}),
            'commentaire': Textarea(attrs={'rows':'5','class':'form-control',}),
        }


class PreprodSearchForm(Form):
    
    
    packid = CharField(required=False, widget= TextInput(attrs={'placeholder': "Pack_id"}) )
    odc = CharField(required=False, widget= TextInput(attrs={'placeholder': 'odc'}) )
    quantite = CharField(required=False, widget= TextInput(attrs={'placeholder': 'quantité'}) )
    date = CharField(required=False, widget= TextInput(attrs={'placeholder': 'date'}) )
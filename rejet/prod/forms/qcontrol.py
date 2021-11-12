from django.forms import ModelForm, fields, Form, DateField, IntegerField,CharField, TextInput, DateInput , Textarea

from prod.models.preprod import Preprod
from prod.models.qcontrol import Qcontrol

class QcontrolForm(ModelForm):
    class Meta:
        model = Qcontrol
        fields = ("date_mise_a_jour","carte_embalee","ab","reprod","autres","commentaire")
        widgets={
            'date_mise_a_jour': TextInput(attrs={'class':'form-control',}),
            'carte_embalee': TextInput(attrs={'class':'form-control',}),
            'ab': TextInput(attrs={'class':'form-control',}),
            'reprod': TextInput(attrs={'class':'form-control',}),
            'autres': TextInput(attrs={'class':'form-control',}),
            'commentaire': Textarea(attrs={'rows':'5','class':'form-control',}),
        }

class QcontrolSearchForm(Form):
    
    packid = CharField(required=False, widget= TextInput(attrs={'placeholder': 'pack_id'}) )
    odc = CharField(required=False, widget= TextInput(attrs={'placeholder': 'odc'}) )
    quantite = CharField(required=False, widget= TextInput(attrs={'placeholder': 'quantité'}) )
from django import forms
from .models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['name','phone_number','description','street','outdoor_number','indoor_number','street2','street3','postal_code','city']
        labels = {'name':'Nombre','phone_number':'Numero de telefono','description':'Descripción','street':'Calle','outdoor_number':'Numero exterior','indoor_number':'Numero interior','street2':'Entre calle 1','street3':'Entre calle 2','postal_code':'Codigo postal','city':'Ciudad'}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class':'form-control'
                })
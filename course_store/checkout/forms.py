from django import forms 
from . import models

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = models.CustomerInfo
        fields = ['card_info']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['card_info'].widget.attrs.update({'class': 'input-form', 
                                                      'placeholder':'Card Number'})
        

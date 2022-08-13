from django.forms import ModelForm
from .models import WalletInstance, BudgetEntry, Category
from django import forms



class WalletForm(ModelForm):

    class Meta:

        model = WalletInstance
        fields = ('name',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                'placeholder': 'Name of a wallet'
            })}

class EntryForm(ModelForm):
    STATE= [
        ('income','income'),
        ('expenses','expenses'),
    ]
    entry_type = forms.ChoiceField(choices = STATE)
    entry_category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label=None)
    wallet_entry_id = forms.CharField(widget=forms.TextInput(attrs={'type': 'hidden'}))

    class Meta:

        model = BudgetEntry
        fields = ('title','amount','description','entry_type','entry_category')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                'placeholder': 'Name of entry'
            }),
            'amount': forms.TextInput(attrs={'class': 'form-control',
                'placeholder': 'Amount'
            }),
            'entry_type': forms.TextInput(attrs={'class': 'form-control',
                'placeholder': 'Income or Expense'
            }),
            'entry_category': forms.TextInput(attrs={'class': 'form-control',
                'placeholder': 'Category'
            }),
            'description': forms.TextInput(attrs={'class': 'form-control',
                'placeholder': 'Description'
            }),
            
            }
            
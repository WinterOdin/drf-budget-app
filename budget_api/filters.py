import django_filters 
from budget_app.models import WalletInstance, BudgetEntry

class WalletFilter(django_filters.FilterSet):

    class Meta:
        model = WalletInstance
        fields = {
            'date_added':['icontains','lte','gte'],
            'entry__entry_category__name':['icontains'],
            'entry__entry_type':['icontains'],
        }

class BudgetFilter(django_filters.FilterSet):

    class Meta:
        model = BudgetEntry
        fields = {
            'date_added':['icontains','lte','gte'],
            'amount':['icontains','lte','gte'],
            'entry_type':['iexact'],
            'entry_category__name':['icontains'],
        }
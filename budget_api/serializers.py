from rest_framework import serializers
from budget_app.models import WalletInstance, BudgetEntry, Category
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models import Sum
from django.db.models import Q
class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'
        


class BudgetEntrySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    
    class Meta:
        model = BudgetEntry
        fields = '__all__'
        depth = 1
        
class WalletInstanceSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    entry = BudgetEntrySerializer(many=True, read_only=True)
    viewable = serializers.SlugRelatedField(many=True, queryset=get_user_model().objects.all(), slug_field='email')
    expense_sum = serializers.SerializerMethodField()
    income_sum = serializers.SerializerMethodField()

    class Meta:
        model = WalletInstance
        fields = '__all__'

    def get_expense_sum(self, obj):
        wallet_obj = WalletInstance.objects.get(id=obj.id)
        return wallet_obj.total_amount('expenses')
    
    def get_income_sum(self, obj):
        wallet_obj = WalletInstance.objects.get(id=obj.id)
        return wallet_obj.total_amount('income')
        
        
    
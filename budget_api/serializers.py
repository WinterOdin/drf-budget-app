from rest_framework import serializers
from budget_app.models import WalletInstance, BudgetEntry, Category
from django.conf import settings
from django.contrib.auth import get_user_model
class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('name',)



class BudgetEntrySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = BudgetEntry
        fields = '__all__'

class WalletInstanceSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    entry = BudgetEntrySerializer(many=True, read_only=True)
    viewable = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all(), many=True)
    

    class Meta:
        model = WalletInstance
        fields = '__all__'
        
        
    
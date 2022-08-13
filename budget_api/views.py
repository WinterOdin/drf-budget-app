from .serializers import WalletInstanceSerializer, BudgetEntrySerializer
from rest_framework.permissions import IsAuthenticated
from budget_app.models import WalletInstance, BudgetEntry
from rest_framework import viewsets
from django.conf import settings
from django.db.models import Q


class WalletViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = WalletInstanceSerializer

    def get_queryset(self):
        user_id = self.request.user.id

        available = WalletInstance.objects.filter(
            Q(owner=user_id) 
        )
        return available

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class BudgetEntryViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BudgetEntrySerializer

    def get_queryset(self):
        user_id = self.request.user.id
        available = BudgetEntry.objects.filter(
            Q(owner=user_id) 
        )
        return available

    def perform_create(self, request):
        form_data = self.request.data
        form_data._mutable = True
        wallet_id = form_data['wallet_entry_id']
        wallet_obj = WalletInstance.objects.get(id=wallet_id)
        if wallet_obj.owner.id == self.request.user.id:
            print(form_data.exclude(wallet_entry_id=wallet_id))
            serializer = BudgetEntrySerializer(data=form_data.pop('wallet_entry_id'))
            if serializer.is_valid():
                serializer.save()
            else:
                print("xD")



    




    


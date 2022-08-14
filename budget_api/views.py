from .serializers import WalletInstanceSerializer, BudgetEntrySerializer
from budget_app.models import WalletInstance, BudgetEntry, Category
from rest_framework.permissions import IsAuthenticated
from .filters import WalletFilter, BudgetFilter
from rest_framework import viewsets
from django.db.models import Q


class WalletViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = WalletInstanceSerializer
    filterset_class = WalletFilter

    def get_queryset(self):
        user_id = self.request.user.id

        available = WalletInstance.objects.filter(
            Q(owner=user_id) |
            Q(viewable = user_id) 
        ).distinct()
        
        return available.order_by('date_added')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BudgetEntryViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BudgetEntrySerializer
    filterset_class = BudgetFilter

    def get_queryset(self):
        user_id = self.request.user.id
        available = BudgetEntry.objects.filter(
            Q(owner=user_id) 
        )
        return available

    def perform_create(self, request):

        form_data = self.request.data.copy()
        wallet_id = form_data['wallet_entry_id']
        wallet_obj = WalletInstance.objects.get(id=wallet_id)
        if wallet_obj.owner.id == self.request.user.id:
            serializer = BudgetEntrySerializer(data=form_data)
            if serializer.is_valid():
                
                #doing this way becaouse if you want to add entry to wallet 
                #wallet can not be serializer instance 

                new_entry = BudgetEntry.objects.create(
                    owner = self.request.user,
                    title = form_data['title'],
                    amount = form_data['amount'],
                    description = form_data['description'],
                    entry_type = form_data['entry_type'],
                    entry_category = Category.objects.get(id=form_data['entry_category']))

                new_entry.save()
                wallet_obj.entry.add(new_entry)
            else:
                print("nah")
                pass
                #user want's to add invalid entry
                #return error on create in serializer
                
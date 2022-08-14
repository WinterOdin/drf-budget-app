from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
import uuid

class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class BudgetEntry(models.Model):
    STATE= [
        ('income','income'),
        ('expenses','expenses'),
    ]
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='owner_of_entry', on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    amount = models.IntegerField()
    description = models.CharField(max_length=60, null=True)
    entry_type = models.CharField(max_length=15, choices=STATE, null=True)
    entry_category = models.ForeignKey(Category, null=True, blank=True, related_name='category_of_entry', on_delete=models.SET_NULL)
    date_added = models.DateField(auto_now_add=True)



class WalletInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=30, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='owner', on_delete=models.CASCADE)
    viewable = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='can_view', blank=True)
    entry = models.ManyToManyField(BudgetEntry, related_name='BudgetEntry', blank=True)
    date_added = models.DateField(auto_now_add=True)

    def total_amount(self, value):
        queryset = self.entry.filter(entry_type=value).aggregate(
            total_amount=models.Sum('amount'))

        if queryset["total_amount"] == None:
            queryset["total_amount"] = 0
        
        return queryset["total_amount"]

    def __str__(self):
        return f'owner: {self.owner} name: {self.name}'

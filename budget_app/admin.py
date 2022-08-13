from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, BudgetEntry, Category, WalletInstance


admin.site.register(User, UserAdmin)
admin.site.register(BudgetEntry)
admin.site.register(Category)
admin.site.register(WalletInstance)

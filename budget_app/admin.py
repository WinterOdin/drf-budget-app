from .models import User, BudgetEntry, Category, WalletInstance
from django.contrib.admin import ModelAdmin, SimpleListFilter
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin


admin.site.register(User, UserAdmin)
admin.site.register(Category)
admin.site.register(WalletInstance)


class RangeFilter(SimpleListFilter):
    title = 'amount filter'
    parameter_name = 'amount'

    def lookups(self, request, model_admin):    
        return ('1', '0-200'),('2', '200-5000'), ('3', '5000-15000'), ('4', '15000-25000'), ('5', '25000-35000')

    def queryset(self, request, queryset):
        filt_amount = request.GET.get('amount')
        amount_dict = dict(self.lookups(None, None))
        if amount_dict.get(filt_amount):
            limiters = amount_dict[filt_amount].split('-')
            return queryset.filter(amount__range=(int(limiters[0]), int(limiters[1])))
        return queryset

        return queryset.filter(amount__range=dict(self.lookups(None, None))[filt_amount])


@admin.register(BudgetEntry)
class BudgetEntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'description', 'date_added')
    search_fields = ('title', 'owner', 'description',)
    list_filter = (RangeFilter,)

from .views import WalletViewset, BudgetEntryViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('wallet', WalletViewset, basename="wallet")
router.register('entry', BudgetEntryViewset, basename="entry")
urlpatterns = router.urls
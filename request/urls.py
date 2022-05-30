from rest_framework.routers import DefaultRouter
from .views import RequestViewSet, FixRequestViewSet, TransferRequestViewSet

router = DefaultRouter()
router.register(r'requests', RequestViewSet)
router.register(r'fix-requests', FixRequestViewSet)
router.register(r'transfer-requests', TransferRequestViewSet)

urlpatterns = router.urls


from rest_framework import routers

from shop.views import BrandViewSet,CategoryViewSet,ProductViewSet

router = routers.SimpleRouter()
router.register(r'brand', BrandViewSet)
router.register(r'accounts', CategoryViewSet)
router.register(r'product', ProductViewSet)
urlpatterns = router.urls
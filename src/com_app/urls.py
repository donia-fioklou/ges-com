from django.urls import path,include
from rest_framework.routers import DefaultRouter
from com_app.views.saleView import SaleViewSet

router = DefaultRouter()
router.register('sales', SaleViewSet)
urlpatterns = [
    path('', include(router.urls)),
]

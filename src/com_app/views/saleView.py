from rest_framework.viewsets import ModelViewSet
from com_app.models.sale import Sale
from com_app.serializers.saleSerialiser import SaleSerializer

class SaleViewSet(ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

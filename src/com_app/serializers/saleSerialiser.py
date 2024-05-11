from rest_framework.serializers import ModelSerializer
from com_app.models.sale import Sale

class SaleSerializer(ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'
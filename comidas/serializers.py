from rest_framework.serializers import ModelSerializer
from comidas.models import Comida

class ComidaParaenseSerializer(ModelSerializer):
    class Meta:
        model = Comida
        fields = '__all__'
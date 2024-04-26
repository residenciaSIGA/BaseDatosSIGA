from rest_framework import serializers
from .models import TipoDoc

class TipoDocSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDoc
        fields = '__all__'
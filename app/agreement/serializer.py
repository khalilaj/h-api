from rest_framework import serializers
from .models import Agreement


class AgreementRetrieveUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agreement
        fields = '__all__'
        read_only_fields = ('id',)


class AgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agreement
        fields = '__all__'
        read_only_fields = ('id',)

    def create(self, validated_data):
            return Agreement.objects.create(**validated_data)
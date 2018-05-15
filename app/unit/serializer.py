from rest_framework import serializers
from .models import Unit


class UnitRetrieveUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'
        read_only_fields = ('id',)


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'
        read_only_fields = ('id',)

    def create(self, validated_data):
            return Unit.objects.create(**validated_data)
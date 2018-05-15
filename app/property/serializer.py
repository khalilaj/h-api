from rest_framework import serializers
from .models import Property


class PropertyRetrieveUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ('id', 'name', 'location', 'year_of_completion',)
        read_only_fields = ('id',)


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ('id', 'name', 'location', 'year_of_completion',)
        read_only_fields = ('id',)

    def create(self, validated_data):
            return Property.objects.create(**validated_data)
from rest_framework import serializers

from .models import Owner


class OwnerRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Owner
        fields = '__all__'


class OwnerListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Owner
        fields = '__all__'
        read_only_fields = ('id', )


class OwnerDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Owner
        fields = '__all__'
        read_only_fields = ('id',)
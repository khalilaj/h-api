from rest_framework import serializers
from .models import Message


class MessageRetrieveUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ('id',)


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ('id',)

    def create(self, validated_data):
            return Message.objects.create(**validated_data)
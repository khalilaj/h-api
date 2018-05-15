from rest_framework import serializers
from .models import Tenant
from ..user.serializer import AccountDetailSerializer
from ..user.models import Account


class TenantSerializer(serializers.ModelSerializer):

    """ This serializer class shows the attributes required to display of the Tenant object
            In this case all the fields are shown
            """

    account = AccountDetailSerializer()

    class Meta:
        model = Tenant
        fields = ('account','id')


class TenantCreateSerializer(serializers.ModelSerializer):

    """
        This serializer class defines how to create a Tenant instance
            """

    email = serializers.EmailField(allow_blank=False)
    username = serializers.CharField(max_length=100, allow_blank=False)
    password = serializers.CharField(max_length=100, allow_blank=False)
    user_type = serializers.CharField(max_length=100, allow_blank=False)
    firstname = serializers.CharField(max_length=100, allow_blank=False)
    lastname = serializers.CharField(max_length=100, allow_blank=False)
    national_id = serializers.CharField(max_length=10, allow_blank=False)
    phone_number = serializers.CharField(max_length=10, allow_blank=False)

    class Meta:
        model = Tenant
        fields = ('national_id', 'phone_number','username', 'password','email','user_type','firstname', 'lastname', )

    def create(self, validated_data):
            return Account.objects.create_user(**validated_data)


class TenantRetrieveUpdateSerial(serializers.ModelSerializer):

    class Meta:
        model = Tenant
        fields = ('account','id')

    def update(self, instance, validated_data):
        account = validated_data.pop('account')
        print(account)
        acc = Account.objects.filter(instance.account.id).update_or_create(account)
        return acc




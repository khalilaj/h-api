from rest_framework import serializers
from .models import Manager
from ..user.serializer import AccountDetailSerializer
from ..user.models import Account


class ManagerSerializer(serializers.ModelSerializer):

    """ This serializer class shows the attributes required to display of the Manager object
            In this case all the fields are shown
            """

    account = AccountDetailSerializer()

    class Meta:
        model = Manager
        fields = '__all__'


class ManagerCreateSerializer(serializers.ModelSerializer):

    """
        This serializer class defines how to create a Manager instance
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
        model = Manager
        fields = ('national_id', 'phone_number','username', 'password','email','user_type','firstname', 'lastname', )

    def create(self, validated_data):
            return Account.objects.create_user(**validated_data)


class ManagerRetrieveUpdateSerial(serializers.ModelSerializer):
    account = AccountDetailSerializer()

    class Meta:
        model = Manager
        fields = '__all__'



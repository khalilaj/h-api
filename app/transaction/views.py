from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from ..agreement.models import Agreement
from ..tenant.models import Tenant
from .permissions import TransactionAccessPermission
from ..core.auth import JwtAuth
from .models import Transaction
from .serializer import TransactionRetrieveUpdateSerializer, TransactionSerializer


class TransactionListCreate(ListCreateAPIView):

    authentication_classes = (JwtAuth,)
    permission_classes = (IsAuthenticated, TransactionAccessPermission)
    serializer_class = TransactionSerializer

    def get_queryset(self):
        if self.request.user.user_type == 'MN':
            return Transaction.objects.all()

        try:
            tenant = Tenant.objects.get(account=self.request.user.id)
        except ObjectDoesNotExist as e:
            pass

        return Transaction.objects.filter(payer=tenant)


    def create(self, request, *args, **kwargs):
        serializer = TransactionSerializer(data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TransactionRetrieveView(RetrieveUpdateDestroyAPIView):
    authentication_classes = (JwtAuth,)
    permission_classes = (IsAuthenticated, TransactionAccessPermission)
    serializer_class = TransactionRetrieveUpdateSerializer

    def get_queryset(self):
        if self.request.user.user_type == 'MN':
            return Transaction.objects.all()

        try:
            tenant = Tenant.objects.get(account=self.request.user.id)
        except ObjectDoesNotExist as e:
            pass

        return Transaction.objects.filter(payer=tenant)
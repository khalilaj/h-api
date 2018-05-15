from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from ..core.auth import JwtAuth
from ..tenant.models import Tenant
from .permissions import AgreementAccessPermission
from .models import Agreement
from .serializer import AgreementRetrieveUpdateSerializer, AgreementSerializer


class AgreementListCreate(ListCreateAPIView):

    authentication_classes = (JwtAuth,)
    permission_classes = (IsAuthenticated, AgreementAccessPermission)
    serializer_class = AgreementSerializer

    def get_queryset(self):
        if self.request.user.user_type == 'MN':
            return Agreement.objects.all()

        try:
            tenant = Tenant.objects.get(account=self.request.user.id)
        except ObjectDoesNotExist as e:
            pass

        return Agreement.objects.filter(tenant=tenant)

    def create(self, request, *args, **kwargs):
        serializer = AgreementSerializer(data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AgreementRetrieveView(RetrieveUpdateDestroyAPIView):
    authentication_classes = (JwtAuth,)
    permission_classes = (IsAuthenticated,)
    serializer_class = (AgreementRetrieveUpdateSerializer)

    def get_queryset(self):
        if self.request.user.user_type == 'MN':
            return Agreement.objects.all()

        try:
            tenant = Tenant.objects.get(account=self.request.user.id)
        except ObjectDoesNotExist as e:
            pass

        return Agreement.objects.filter(tenant=tenant)
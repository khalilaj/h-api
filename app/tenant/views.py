from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from ..core.auth import JwtAuth
from .permissions import TenantAccessPermission

from .models import Tenant
from .serializer import TenantSerializer, TenantCreateSerializer, TenantRetrieveUpdateSerial


class TenantListCreate(ListCreateAPIView):
    authentication_classes = (JwtAuth,)
    permission_classes = (IsAuthenticated, TenantAccessPermission,)
    serializer_class = TenantSerializer

    def get_queryset(self):
        if self.request.user.user_type == 'MN':
            return Tenant.objects.all()

        return Tenant.objects.filter(account=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = TenantCreateSerializer(data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TenantRetrieve(RetrieveUpdateDestroyAPIView):
    authentication_classes = (JwtAuth,)
    permission_classes = (IsAuthenticated,)
    serializer_class = (TenantRetrieveUpdateSerial)

    def get_queryset(self):
        if self.request.user.user_type == 'MN':
            return Tenant.objects.all()

        return Tenant.objects.filter(account=self.request.user)


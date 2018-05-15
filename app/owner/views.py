from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from ..core.auth import JwtAuth
from .permissions import OwnerAccessPermission
from .serializer import OwnerListSerializer, OwnerRetrieveSerializer
from .models import Owner


class OwnerListCreate(ListCreateAPIView):

    authentication_classes = (JwtAuth,)
    permission_classes = (IsAuthenticated, OwnerAccessPermission)
    serializer_class = OwnerListSerializer

    def get_queryset(self):
            return Owner.objects.all()

class OwnerRetrieveView(RetrieveUpdateDestroyAPIView):
    authentication_classes = (JwtAuth,)
    permission_classes = (IsAuthenticated, OwnerAccessPermission)
    serializer_class = OwnerRetrieveSerializer

    def get_queryset(self):
            return Owner.objects.all()

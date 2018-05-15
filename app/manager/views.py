from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from ..core.auth import JwtAuth
from .permissions import ManagerAccessPermission

from .models import Manager
from .serializer import ManagerSerializer, ManagerCreateSerializer, ManagerRetrieveUpdateSerial


class ManagerListCreate(ListCreateAPIView):
    authentication_classes = (JwtAuth,)
    permission_classes = (IsAuthenticated, ManagerAccessPermission,)
    serializer_class = ManagerSerializer

    def get_queryset(self):
            return Manager.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = ManagerCreateSerializer(data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ManagerRetrieve(RetrieveUpdateDestroyAPIView):
    authentication_classes = (JwtAuth,)
    permission_classes = (IsAuthenticated, ManagerAccessPermission)
    serializer_class = ManagerRetrieveUpdateSerial

    def get_queryset(self):
            return Manager.objects.all()



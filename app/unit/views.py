from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from ..unit.permissions import UnitAccessPermission
from ..core.auth import JwtAuth
from .models import Unit
from .serializer import UnitRetrieveUpdateSerializer, UnitSerializer


class UnitListCreate(ListCreateAPIView):

    authentication_classes = (JwtAuth,)
    permission_classes = (IsAuthenticated, UnitAccessPermission)
    serializer_class = UnitSerializer

    def get_queryset(self):
        return Unit.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = UnitSerializer(data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UnitRetrieveView(RetrieveUpdateDestroyAPIView):
    authentication_classes = (JwtAuth,)
    permission_classes = (IsAuthenticated, UnitAccessPermission)
    serializer_class = (UnitRetrieveUpdateSerializer)

    def get_queryset(self):
        return Unit.objects.all()
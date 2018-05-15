from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from ..core.auth import JwtAuth
from .models import Property
from .serializer import PropertyRetrieveUpdateSerializer, PropertySerializer


class PropertyListCreate(ListCreateAPIView):

    authentication_classes = (JwtAuth,)
    permission_classes = (IsAuthenticated,)
    serializer_class = PropertySerializer

    def get_queryset(self):
        return Property.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = PropertySerializer(data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PropertyRetrieveView(RetrieveUpdateDestroyAPIView):
    authentication_classes = (JwtAuth,)
    permission_classes = (IsAuthenticated,)
    serializer_class = (PropertyRetrieveUpdateSerializer)

    def get_queryset(self):
        return Property.objects.all()
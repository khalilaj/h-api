from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from ..message.permissions import MessageAccessPermission
from ..tenant.models import Tenant
from ..core.auth import JwtAuth
from .models import Message
from .serializer import MessageRetrieveUpdateSerializer, MessageSerializer


class MessageListCreate(ListCreateAPIView):

    authentication_classes = (JwtAuth,)
    permission_classes = (IsAuthenticated,MessageAccessPermission)
    serializer_class = MessageSerializer

    def get_queryset(self):
        if self.request.user.user_type == 'MN':
            return Message.objects.all()

        try:
            tenant = Tenant.objects.get(account=self.request.user.id)
        except ObjectDoesNotExist as e:
            pass

        return Message.objects.filter(tenant=tenant)

    def create(self, request, *args, **kwargs):
        serializer = MessageSerializer(data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MessageRetrieveView(RetrieveUpdateDestroyAPIView):
    authentication_classes = (JwtAuth,)
    permission_classes = (IsAuthenticated, MessageAccessPermission,)
    serializer_class = MessageRetrieveUpdateSerializer

    def get_queryset(self):
        if self.request.user.user_type == 'MN':
            return Message.objects.all()

        try:
            tenant = Tenant.objects.get(account=self.request.user.id)
        except ObjectDoesNotExist as e:
            pass

        return Message.objects.filter(tenant=tenant)
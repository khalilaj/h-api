from django.conf.urls import url
from .views import MessageListCreate, MessageRetrieveView

urlpatterns = [
    url(r'^$', MessageListCreate.as_view(), name='list-create-message'),
    url(r'^(?P<pk>\d+)$', MessageRetrieveView.as_view(), name='retrieve-message'),
]

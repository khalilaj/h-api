from django.conf.urls import url
from .views import OwnerListCreate, OwnerRetrieveView

urlpatterns = [
    url(r'^$', OwnerListCreate.as_view(), name='list-create-owner'),
    url(r'^(?P<pk>\d+)$', OwnerRetrieveView.as_view(), name='retrieve-owner'),
]

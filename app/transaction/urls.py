from django.conf.urls import url
from .views import TransactionListCreate, TransactionRetrieveView

urlpatterns = [
    url(r'^$', TransactionListCreate.as_view(), name='list-create-transaction'),
    url(r'^(?P<pk>\d+)$', TransactionRetrieveView.as_view(), name='retrieve-transaction+'),
]

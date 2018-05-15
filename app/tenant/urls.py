from django.conf.urls import url
from .views import TenantListCreate, TenantRetrieve

urlpatterns = [
    url(r'^$', TenantListCreate.as_view(), name='list-create-tenant'),
    url(r'^(?P<pk>\d+)$', TenantRetrieve.as_view(), name='retrieve-tenant'),
]


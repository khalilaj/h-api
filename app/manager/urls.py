from django.conf.urls import url
from .views import ManagerListCreate, ManagerRetrieve

urlpatterns = [
    url(r'^$', ManagerListCreate.as_view(), name='list-create-manager'),
    url(r'^(?P<pk>\d+)$', ManagerRetrieve.as_view(), name='retrieve-manager'),
]

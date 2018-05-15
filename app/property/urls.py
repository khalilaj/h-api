from django.conf.urls import url
from .views import PropertyListCreate, PropertyRetrieveView

urlpatterns = [
    url(r'^$', PropertyListCreate.as_view(), name='list-create-property'),
    url(r'^(?P<pk>\d+)$', PropertyRetrieveView.as_view(), name='retrieve-property'),
]

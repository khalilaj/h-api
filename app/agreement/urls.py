from django.conf.urls import url
from .views import AgreementListCreate, AgreementRetrieveView

urlpatterns = [
    url(r'^$', AgreementListCreate.as_view(), name='list-create-agreement'),
    url(r'^(?P<pk>\d+)$', AgreementRetrieveView.as_view(), name='retrieve-agreement'),
]

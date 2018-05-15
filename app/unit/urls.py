from django.conf.urls import url
from .views import UnitListCreate, UnitRetrieveView

urlpatterns = [
    url(r'^$', UnitListCreate.as_view(), name='list-create-unit'),
    url(r'^(?P<pk>\d+)$', UnitRetrieveView.as_view(), name='retrieve-unit'),
]

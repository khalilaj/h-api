from django.conf.urls import include,url
from .user import views

urlpatterns = [
    url(r'^login/', views.LoginView.as_view()),
    url(r'^register/', views.RegistrationView.as_view()),
    url(r'^user/', include('app.user.urls')),
    url(r'^tenant/', include('app.tenant.urls')),
    url(r'^manager/', include('app.manager.urls')),
    url(r'^owner/', include('app.owner.urls')),
    url(r'^property/', include('app.property.urls')),
    url(r'^unit/', include('app.unit.urls')),
    url(r'^agreement/', include('app.agreement.urls')),
    url(r'^message/', include('app.message.urls')),
    url(r'^transaction/', include('app.transaction.urls')),

]

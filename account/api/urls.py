from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import registration_api, account_update_api, account_view_api, ObtainAuthTokenView
app_name="account"
urlpatterns = [
    path("register", csrf_exempt(registration_api), name="register"),
    path("login", ObtainAuthTokenView.as_view(), name="login"),
    path("update", account_update_api, name="update"),
    path("detail", account_view_api, name="detail"),
]
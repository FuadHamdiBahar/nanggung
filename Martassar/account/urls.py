from django.urls import path

from . views import (
    AccountLoginView,
    AccountLogoutView,
    RegisterView,
)

app_name = 'account'
urlpatterns = [
    path('', RegisterView, name='register'),
    path('login/', AccountLoginView.as_view(), name='login'),
    path('logout/', AccountLogoutView.as_view(), name='logout')
]

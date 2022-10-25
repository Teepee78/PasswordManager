from django.urls import path
from accounts.api import views


app_name = 'accounts'
urlpatterns = [
    path('', views.AccountsView.as_view(), name='accounts_view'),
    path('<int:pk>/', views.AccountView.as_view(), name='account_view')
]

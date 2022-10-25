from rest_framework import status, generics
from accounts.models import CustomUser
from accounts.api.serializers import UserSerializer


class AccountsView(generics.ListCreateAPIView):
    """
    List all users
    """

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class AccountView(generics.RetrieveUpdateDestroyAPIView):
    """
    Lists a requested account
    """

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

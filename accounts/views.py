from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView

from accounts.models import Account
from accounts.serializers import AccountSerializer


class CreateAccountView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class LoginView(TokenObtainPairView):
    pass

#class LoginView(TokenObtainPairView):
    #pass

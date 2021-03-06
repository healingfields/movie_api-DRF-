from .serializers import RegisterSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import  status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from . import models
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['POST'])
def register_view(request):

    if request.method == 'POST':
        data = {}
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            data['username'] = account.username
            data['email'] = account.email
            token = Token.objects.get(user=account).key
            data['token'] = token
            # refresh = RefreshToken.for_user(account)
            # data['token'] = {
            #     'refresh': str(refresh),
            #     'access': str(refresh.access_token),
            # }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
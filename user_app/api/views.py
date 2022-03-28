from .serializers import RegisterSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from . import models


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
            return Response(data)
        return Response(serializer.errors)


from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .serializers import AccountSerializer, UserAccountSerializer
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from django.contrib.auth.models import User

@api_view(["POST",])
@permission_classes([])
@authentication_classes([])
def registration_api(request):
    context = {
        "success": False
    }
    serializer = AccountSerializer(data=request.data)
    if serializer.is_valid():
        account = serializer.save()
        token = Token.objects.get(user=account).key
        context = {
            "success": True,
            "id": account.id,
            "username": account.username,
            "email": account.email,
            "token" : token
        }
        return Response(data=context,status=status.HTTP_201_CREATED)
    else:
        context["error"] = serializer.errors
        return Response(context)

@api_view(["PUT"])
@permission_classes((IsAuthenticated,))
def account_update_api(request):
    try:
        account = request.user
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = UserAccountSerializer(account, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={"success": "user successfully update"})
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def account_view_api(request):
    try:
        account = request.user
    except User.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    serializer = UserAccountSerializer(account)
    return Response(data=serializer.data)

class ObtainAuthTokenView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        context = {}
        username = request.POST.get('username')
        password = request.POST.get('password')
        userobj = authenticate(username=username, password=password)
        if userobj:
            try:
                token = Token.objects.get(user=userobj)
            except Token.DoesNotExist:
                token = Token.objects.create(user=userobj)
            context['success'] = True
            context['token'] = token.key
        else:
            context['success'] = False
            context["message"] = "incorrect login credential"
        return Response(context)

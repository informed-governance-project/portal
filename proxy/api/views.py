from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from portal.models import ExternalToken, Module, User

from .serializers import (
    ExternalTokenInputSerializer,
    ExternalTokenSerializer,
    ModuleInputSerializer,
    ModuleSerializer,
    UserInputSerializer,
    UserSerializer,
)


#
# Model: ExternalToken
#
class ExternalTokenApiView(APIView):
    # add permission to check if user is authenticated
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    @extend_schema(request=None, responses=ExternalTokenSerializer)
    def get(self, request, *args, **kwargs):
        """
        List all the external tokens.
        """
        objects = ExternalToken.objects.all()
        serializer = ExternalTokenSerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        request=ExternalTokenInputSerializer, responses=ExternalTokenSerializer
    )
    def post(self, request, *args, **kwargs):
        """
        Create a new access for a user to the specified service.
        """
        try:
            user = User.objects.get(username=request.data["username"])
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            module = Module.objects.get(name=request.data["module_name"])
        except Module.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            if not request.data.get("token", False):
                del request.data["token"]
        except Exception:
            pass

        new_external_token = ExternalToken.objects.create(
            user=user,
            module=module,
        )
        serializer = ExternalTokenSerializer(new_external_token)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ExternalTokenApiElemView(GenericAPIView):
    # add permission to check if user is authenticated
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = ExternalTokenSerializer

    @extend_schema(
        request=ExternalTokenInputSerializer, responses=ExternalTokenSerializer
    )
    def put(self, request, id=None):
        """
        Update an existing token.
        """
        external_token = ExternalToken.objects.get(id=id)
        external_token.token = request.data["token"]
        external_token.save()
        serializer = ExternalTokenSerializer(external_token)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id=None):
        """
        Revoke a user's access.
        """
        external_token = ExternalToken.objects.filter(id=id)
        external_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#
# Model: User
#
class UserApiView(APIView):
    # add permission to check if user is authenticated
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    @extend_schema(request=None, responses=UserSerializer)
    def get(self, request, *args, **kwargs):
        """
        List all the users.
        """
        objects = User.objects.all()
        serializer = UserSerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Create a new object
    @extend_schema(request=UserInputSerializer, responses=UserSerializer)
    def post(self, request, *args, **kwargs):
        """
        Create a new user.
        """
        new_user = User.objects.create(
            username=request.data["username"],
            email=request.data["email"],
            is_regulator=request.data["is_regulator"],
            is_staff=request.data["is_staff"],
        )
        new_user.set_password(request.data["password"])
        new_user.save()
        serializer = UserSerializer(new_user)
        return Response(serializer.data, status=status.HTTP_200_OK)


#
# Model: Module
#
class ModuleApiView(APIView):
    # add permission to check if user is authenticated
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    @extend_schema(request=None, responses=ModuleSerializer)
    def get(self, request, *args, **kwargs):
        """
        List all the modules.
        """
        objects = Module.objects.all()
        serializer = ModuleSerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Create a new object
    @extend_schema(request=ModuleInputSerializer, responses=ModuleSerializer)
    def post(self, request, *args, **kwargs):
        """
        Create a new module.
        """
        new_module = Module.objects.create(
            name=request.data["name"],
            path=request.data["path"],
            upstream=request.data["upstream"],
            authentication_required=request.data["authentication_required"],
        )
        serializer = ModuleSerializer(new_module)
        return Response(serializer.data, status=status.HTTP_200_OK)

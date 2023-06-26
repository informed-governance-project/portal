from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from proxy.models import ExternalToken, User

from .serializers import ExternalTokenInputSerializer, ExternalTokenSerializer

#
# Model: ExternalToken
#


class ExternalTokenApiView(APIView):
    # add permission to check if user is authenticated
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    # List all
    @extend_schema(request=None, responses=ExternalTokenSerializer)
    def get(self, request, *args, **kwargs):
        """
        List all the items.
        """
        objects = ExternalToken.objects.all()
        serializer = ExternalTokenSerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Create a new object
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

        new_external_token = ExternalToken.objects.create(
            user=user,
            module_name=request.data["module_name"],
            module_path=request.data["module_path"],
            token=request.data["token"],
        )
        serializer = ExternalTokenSerializer(new_external_token)
        return Response(serializer.data, status=status.HTTP_200_OK)

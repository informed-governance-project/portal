from rest_framework import serializers

from portal.models import ExternalToken, User


class ExternalTokenInputSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=200)
    # module_name = serializers.CharField(max_length=200)
    # module_path = serializers.CharField(max_length=200)
    token = serializers.CharField(max_length=200)

    class Meta:
        model = ExternalToken
        fields = [
            "id",
            "username",
            # "module_name",
            # "module_path",
            "token",
        ]


class ExternalTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalToken
        fields = ["id", "module_name", "module_path"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "is_staff", "is_regulator"]


class UserInputSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    is_staff = serializers.BooleanField()
    is_regulator = serializers.BooleanField()
    password = serializers.CharField(max_length=200)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "is_staff",
            "is_regulator",
            "password",
        ]

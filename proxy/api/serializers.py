from rest_framework import serializers

from portal.models import ExternalToken, Module, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "is_staff", "is_regulator"]


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ["name", "path", "upstream", "authentication_required"]


class ModuleInputSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200, required=True)
    path = serializers.CharField(max_length=200, required=True)
    upstream = serializers.CharField(max_length=200, required=True)
    authentication_required = serializers.BooleanField(default=True)

    class Meta:
        model = Module
        fields = [
            "name",
            "path",
            "upstream",
            "authentication_required",
        ]


class ExternalTokenInputSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=200, required=True)
    module_name = serializers.CharField(max_length=200, required=True)
    token = serializers.CharField(max_length=200)

    class Meta:
        model = ExternalToken
        fields = [
            "id",
            "username",
            "module_name",
            "token",
        ]


class ExternalTokenSerializer(serializers.ModelSerializer):
    module = ModuleSerializer(many=False, read_only=True)
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = ExternalToken
        fields = ["id", "module", "user", "token"]


class UserInputSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=200, required=True)
    email = serializers.CharField(max_length=200, required=True)
    is_staff = serializers.BooleanField(default=False)
    is_regulator = serializers.BooleanField(default=False)
    password = serializers.CharField(max_length=200, required=True)

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

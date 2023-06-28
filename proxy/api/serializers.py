from rest_framework import serializers

from portal.models import ExternalToken


class ExternalTokenInputSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=200)
    module_name = serializers.CharField(max_length=200)
    module_path = serializers.CharField(max_length=200)
    token = serializers.CharField(max_length=200)

    class Meta:
        model = ExternalToken
        fields = ["id", "username", "module_name", "module_path", "token"]


class ExternalTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalToken
        fields = ["id", "module_name", "module_path"]

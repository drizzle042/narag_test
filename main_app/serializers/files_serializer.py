from rest_framework.serializers import ModelSerializer
from base_app.models import Files


class FileSerializer(ModelSerializer):
    class Meta:
        model = Files
        fields = "__all__"
        
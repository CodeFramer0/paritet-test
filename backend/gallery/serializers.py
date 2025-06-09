import base64
import uuid

from django.core.files.base import ContentFile
from rest_framework import serializers

from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    image_base64 = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Image
        fields = ["id", "image", "description", "image_base64"]
        read_only_fields = ["id", "image"]

    def create(self, validated_data):
        base64_data = validated_data.pop("image_base64", None)
        if base64_data:
            format, imgstr = base64_data.split(";base64,")
            ext = format.split("/")[-1]
            file_name = f"{uuid.uuid4()}.{ext}"
            validated_data["image"] = ContentFile(
                base64.b64decode(imgstr), name=file_name
            )
        return super().create(validated_data)

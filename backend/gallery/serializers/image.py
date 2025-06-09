import base64
import uuid

from django.core.files.base import ContentFile
from rest_framework import serializers

from gallery.models import Image


class ImageSerializer(serializers.ModelSerializer):
    image_base64 = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Image
        fields = ["id", "image", "description", "image_base64"]
        read_only_fields = ["id", "image"]

    def create(self, validated_data):
        base64_str = validated_data.pop("image_base64", None)
        if base64_str:
            validated_data["image"] = self._decode_base64_image(base64_str)
        return super().create(validated_data)

    def _decode_base64_image(self, base64_string: str) -> ContentFile:
        try:
            format, data = base64_string.split(";base64,")
            ext = format.split("/")[-1]
            file_name = f"{uuid.uuid4()}.{ext}"
            return ContentFile(base64.b64decode(data), name=file_name)
        except Exception:
            raise serializers.ValidationError("Invalid base64 image format")

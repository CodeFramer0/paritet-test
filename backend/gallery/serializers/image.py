import base64
import uuid

from django.core.files.base import ContentFile
from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from gallery.models import Image


class ImageSerializer(serializers.ModelSerializer):
    image = Base64ImageField()

    class Meta:
        model = Image
        fields = ["id", "image", "description",]
        read_only_fields = ["id",]

from rest_framework import serializers

from .models import Property, PropertyImage


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ["image", "alt_text"]


class PropertySerializer(serializers.ModelSerializer):
    product_image = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Property
        fields = "__all__"

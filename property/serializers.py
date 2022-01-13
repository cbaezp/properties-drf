from agent.serializers import AgentSerializer, AgentSerializerPreview
from rest_framework import serializers

from .models import (
    Category,
    Property,
    PropertyImage,
    PropertySpecification,
    PropertySpecificationValue,
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ["image", "alt_text"]


class PropertySpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertySpecification
        fields = ["name"]


class PropertySpecificationValueSerializer(serializers.ModelSerializer):
    specification = PropertySpecificationSerializer(read_only=True)

    class Meta:
        model = PropertySpecificationValue
        fields = ["specification", "value"]


class PropertySerializer(serializers.ModelSerializer):

    property_image = ImageSerializer(many=True, read_only=True)
    agent = AgentSerializerPreview(read_only=True)
    category = CategorySerializer(read_only=True)
    property_specification_value = PropertySpecificationValueSerializer(many=True, read_only=True)

    class Meta:
        model = Property
        fields = "__all__"

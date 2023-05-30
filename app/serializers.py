from rest_framework import serializers

from .models import Image


class uploadImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'







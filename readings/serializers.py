from rest_framework import serializers
from readings.models import Reading


class ReadingsSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.user_id")
    class Meta:
        model = Reading
        fields = '__all__'

from rest_framework import serializers
from .models import ad

class ad_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ad
        fields = ["id", "description", "email", "state", "category"]


from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
            "contact_no",
            "gender",
            "address",
            "landmark",
            "city",
            "state",
            "country",
            "pincode"
        )

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

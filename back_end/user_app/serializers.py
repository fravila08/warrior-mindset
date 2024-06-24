from rest_framework import serializers
from .models import AppUser


class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        # Include all the fields you want to expose in the API
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "username",
            "is_active",
            "date_joined",
        ]
        read_only_fields = [
            "id",
            "is_active",
            "date_joined",
        ]  # Fields that should not be editable

    def create(self, validated_data: dict) -> AppUser:
        # Use the custom manager to create a user, ensuring the proper defaults for is_staff and is_superuser
        user = AppUser.objects.create_user(**validated_data)
        return user

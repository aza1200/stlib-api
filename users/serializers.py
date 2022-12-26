from rest_framework.serializers import ModelSerializer
from .models import User


class TinyUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "avatar",
            "username"
        )

class PrivateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "password",
            "is_superuser",
            "is_staff",
            "id",
            "is_active",
            "name",
            "first_name",
            "last_name",
            "groups",
            "user_permissions" 
        )
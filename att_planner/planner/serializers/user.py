from rest_framework import serializers

from att_planner.planner.models.user import User


class UserWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email_id', 'user_name', 'is_active', 'last_login')


class UserReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

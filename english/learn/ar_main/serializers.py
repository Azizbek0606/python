from rest_framework import serializers
from .models import User, Activity, Badge, Leaderboard

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'level', 'total_points', 'streak', 'last_activity', 'created_at', 'is_active']
        read_only_fields = ['total_points', 'streak', 'last_activity', 'created_at']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'level']

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            level=validated_data.get('level', 'beginner')
        )
        return user

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'user', 'points_earned', 'activity_date', 'completed_at', 'description']
        read_only_fields = ['completed_at']

class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = ['id', 'user', 'badge_name', 'badge_description', 'awarded_at']
        read_only_fields = ['awarded_at']

class LeaderboardSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Leaderboard
        fields = ['id', 'user', 'username', 'week_start_date', 'total_points', 'rank']
        read_only_fields = ['rank']
from django.contrib import admin
from .models import User, Activity, Badge, Leaderboard

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'level', 'total_points', 'streak', 'is_active']
    search_fields = ['username', 'email']
    list_filter = ['level', 'is_active']

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['user', 'points_earned', 'activity_date', 'completed_at']
    search_fields = ['user__username']
    list_filter = ['activity_date']

@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    list_display = ['user', 'badge_name', 'awarded_at']
    search_fields = ['user__username', 'badge_name']
    list_filter = ['awarded_at']

@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ['user', 'week_start_date', 'total_points', 'rank']
    search_fields = ['user__username']
    list_filter = ['week_start_date']
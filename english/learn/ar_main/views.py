from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.utils import timezone
from datetime import timedelta
from .models import User, Activity, Badge, Leaderboard
from .serializers import UserSerializer, RegisterSerializer, ActivitySerializer, BadgeSerializer, LeaderboardSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticated()]

    def create(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'])
    def profile(self, request, pk=None):
        user = self.get_object()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
        user.total_points += serializer.validated_data['points_earned']

        today = timezone.now().date()
        last_activity = user.last_activity.date()
        if last_activity == today - timedelta(days=1):
            user.streak += 1
        elif last_activity < today - timedelta(days=1):
            user.streak = 0
        user.last_activity = timezone.now()
        user.save()

        # Badge tekshiruvi
        if user.total_points >= 100 and not Badge.objects.filter(user=user, badge_name="Beginner Star").exists():
            Badge.objects.create(
                user=user,
                badge_name="Beginner Star",
                badge_description="Reached 100 points"
            )
        if user.streak >= 7 and not Badge.objects.filter(user=user, badge_name="Streak Master").exists():
            Badge.objects.create(
                user=user,
                badge_name="Streak Master",
                badge_description="7-day streak achieved"
            )


class BadgeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Badge.objects.filter(user=self.request.user)


class LeaderboardViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LeaderboardSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        week_start = timezone.now().date() - timedelta(days=timezone.now().weekday())
        queryset = Leaderboard.objects.filter(week_start_date=week_start).order_by('-total_points')
        for index, entry in enumerate(queryset, start=1):
            entry.rank = index
            entry.save()
        return queryset

    @action(detail=False, methods=['get'])
    def current_week(self, request):
        week_start = timezone.now().date() - timedelta(days=timezone.now().weekday())
        # Har bir foydalanuvchi uchun leaderboard yozuvini yangilash
        users = User.objects.filter(is_active=True)
        for user in users:
            weekly_points = Activity.objects.filter(
                user=user,
                activity_date__gte=week_start,
                activity_date__lte=week_start + timedelta(days=6)
            ).aggregate(models.Sum('points_earned'))['points_earned__sum'] or 0
            Leaderboard.objects.update_or_create(
                user=user,
                week_start_date=week_start,
                defaults={'total_points': weekly_points}
            )
        return self.list(request)
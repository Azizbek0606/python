from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('Email kiritilishi shart')
        if not username:
            raise ValueError('Username kiritilishi shart')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, username, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    level = models.CharField(max_length=20, default="beginner")  # beginner, intermediate, advanced
    total_points = models.IntegerField(default=0)
    streak = models.IntegerField(default=0)
    last_activity = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='ar_main_user_groups',
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='ar_main_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.'
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.username

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    points_earned = models.IntegerField(default=0)
    activity_date = models.DateField(default=timezone.now)
    completed_at = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=200, blank=True)

    class Meta:
        db_table = "activities"

    def __str__(self):
        return f"{self.user.username} - {self.points_earned} points - {self.activity_date}"

class Badge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='badges')
    badge_name = models.CharField(max_length=50)
    badge_description = models.CharField(max_length=200, blank=True)
    awarded_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "badges"

    def __str__(self):
        return f"{self.user.username} - {self.badge_name}"

class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leaderboard_entries')
    week_start_date = models.DateField()
    total_points = models.IntegerField(default=0)
    rank = models.IntegerField(null=True)

    class Meta:
        db_table = "leaderboard"
        unique_together = ('user', 'week_start_date')

    def __str__(self):
        return f"{self.user.username} - {self.total_points} points - Week {self.week_start_date}"
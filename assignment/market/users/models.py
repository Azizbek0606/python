from django.contrib.auth.models import User
from django.db import models


class Users(models.Model):
    ROLE_CHOICES = [
        ("admin", "Admin"),
        ("customer", "Customer"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="customer")
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} ({self.role})"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

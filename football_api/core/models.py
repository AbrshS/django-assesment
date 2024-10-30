from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """
    Custom user model that includes user roles such as admin, coach, agent, and football player.
    """
    ADMIN = 'admin'
    COACH = 'coach'
    AGENT = 'agent'
    FOOTBALL_PLAYER = 'football_player'
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (COACH, 'Coach'),
        (AGENT, 'Agent'),
        (FOOTBALL_PLAYER, 'Football Player'),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=FOOTBALL_PLAYER,
        help_text="Defines the role of the user (e.g., admin, coach, agent, football player)."
    )

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

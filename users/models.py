from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    #using AbstractUser to extend the default user model
    #adding a role field to differentiate between students and librarians
    ROLE_CHOICES = (
        ("student", "Student"),
        ("librarian", "Librarian"),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

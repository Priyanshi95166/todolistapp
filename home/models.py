from django.db import models


class Task(models.Model):
    PRIORITY_HIGH = "High"
    PRIORITY_MEDIUM = "Medium"
    PRIORITY_LOW = "Low"

    PRIORITY_CHOICES = [
        (PRIORITY_HIGH, "High"),
        (PRIORITY_MEDIUM, "Medium"),
        (PRIORITY_LOW, "Low"),
    ]

    content = models.CharField(max_length=255)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.content

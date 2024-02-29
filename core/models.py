from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    duedate = models.DateField()
    complete = models.BooleanField(default=False)
    completed_at = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.complete and not self.completed_at:
            self.completed_at = timezone.now().date()
        elif not self.complete:
            self.completed_at = None  # Set completed_at to None when complete is False
        super().save(*args, **kwargs)

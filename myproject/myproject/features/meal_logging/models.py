from django.db import models
from django.contrib.auth.models import User

class MealLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal_description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s meal: {self.meal_description[:30]}"
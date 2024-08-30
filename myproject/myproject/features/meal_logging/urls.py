from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import MealLogViewSet

router = DefaultRouter()
router.register(r'meal-logs', MealLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import MealLog

class MealLogViewSet(viewsets.ModelViewSet):
    queryset = MealLog.objects.all()
    
    @action(detail=False, methods=['post'])
    def log_meal(self, request):
        user = request.user  # Assuming you have authentication set up
        meal_description = request.data.get('meal_description')
        
        meal_log = MealLog.objects.create(user=user, meal_description=meal_description)
        
        return Response({"status": "success", "message": "Meal logged successfully"})
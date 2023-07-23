from django.shortcuts import render
from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view




# Create your views here.
@api_view(['GET'])
def drinks_list(request):
    drink = Drink.objects.all()
    serializer = DrinkSerializer(drink, many=True)
    return JsonResponse(serializer.data, safe=False)
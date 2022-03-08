from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .models import User, Investment, Bill
from .serializers import UserSerializer, InvestmentSerializer, BillSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class InvestmentViewSet(viewsets.ModelViewSet):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer

class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

@api_view(['GET'])
def investments_per_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    investments = Investment.objects.filter(user=user).order_by('investment_date')
    serializer = InvestmentSerializer(investments, many=True, context={'request': request})
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def bills_per_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    bills = Bill.objects.filter(user=user).order_by('bill_date')
    serializer = BillSerializer(bills, many=True, context={'request': request})
    return JsonResponse(serializer.data, safe=False)

@api_view(['PUT', 'DELETE'])
def edit_investment(request, pk):
    investment = get_object_or_404(Investment, pk=pk)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = InvestmentSerializer(investment, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        investment.delete()
        return JsonResponse(status=204)



